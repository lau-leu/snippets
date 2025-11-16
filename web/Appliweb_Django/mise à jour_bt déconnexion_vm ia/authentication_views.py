from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django_otp.decorators import otp_required
from django_otp.plugins.otp_email.models import EmailDevice
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import LoginAttempt, ChatConversation, ChatMessage
from .ollama_service import OllamaService
import json


def get_client_ip(request):
    """Obtenir l'IP du client"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@login_required
def setup_2fa_choice(request):
    """Choisir la méthode 2FA"""

    # Vérifier si l'utilisateur a déjà configuré la 2FA
    has_totp = TOTPDevice.objects.filter(user=request.user, confirmed=True).exists()
    has_email = EmailDevice.objects.filter(user=request.user, confirmed=True).exists()

    if has_totp or has_email:
        return redirect('hello')

    if request.method == 'POST':
        method = request.POST.get('method')

        if method == 'email':
            # Créer un device email
            device = EmailDevice.objects.create(
                user=request.user,
                name='default',
                email=request.user.email,
                confirmed=True
            )
            messages.success(request, "Authentification par email activée !")
            return redirect('hello')

        elif method == 'authenticator':
            # Rediriger vers le setup standard de two_factor
            return redirect('two_factor:setup')

    return render(request, 'authentication/setup_2fa_choice.html')


@login_required
@otp_required
def hello_view(request):
    """Page Hello World - accessible après authentification complète"""

    # Enregistrer la tentative réussie
    LoginAttempt.objects.create(
        user=request.user,
        username=request.user.username,
        ip_address=get_client_ip(request),
        success=True,
        two_fa_completed=True,
        user_agent=request.META.get('HTTP_USER_AGENT', '')
    )

    context = {
        'user': request.user
    }

    return render(request, 'authentication/hello.html', context)


def logout_view(request):
    """Déconnexion"""
    logout(request)
    messages.info(request, "Vous avez été déconnecté avec succès")
    return redirect('two_factor:login')


@login_required
@otp_required
def ai_chat_view(request):
    """Page de chat avec l'IA Ollama"""

    ollama = OllamaService()

    # Récupérer les modèles disponibles
    available_models = ollama.get_available_models()

    # Récupérer les conversations de l'utilisateur
    conversations = ChatConversation.objects.filter(user=request.user)

    # Conversation active (la plus récente ou nouvelle)
    conversation_id = request.GET.get('conversation_id')
    if conversation_id:
        conversation = get_object_or_404(ChatConversation, id=conversation_id, user=request.user)
    else:
        conversation = conversations.first()

    # Récupérer les messages de la conversation
    messages_list = []
    if conversation:
        messages_list = conversation.messages.all()

    context = {
        'available_models': available_models,
        'conversations': conversations,
        'current_conversation': conversation,
        'messages': messages_list,
        'default_model': ollama.default_model if available_models else None
    }

    return render(request, 'authentication/ai_chat.html', context)


@login_required
@otp_required
@require_POST
def ai_chat_send(request):
    """Envoyer un message à l'IA"""

    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        model_name = data.get('model')
        conversation_id = data.get('conversation_id')

        if not user_message:
            return JsonResponse({'success': False, 'error': 'Message vide'})

        ollama = OllamaService()

        # Récupérer ou créer la conversation
        if conversation_id:
            conversation = get_object_or_404(ChatConversation, id=conversation_id, user=request.user)
        else:
            # Créer une nouvelle conversation
            conversation = ChatConversation.objects.create(
                user=request.user,
                title=user_message[:50] + ('...' if len(user_message) > 50 else ''),
                model_name=model_name
            )

        # Sauvegarder le message de l'utilisateur
        ChatMessage.objects.create(
            conversation=conversation,
            role='user',
            content=user_message
        )

        # Construire l'historique pour le contexte
        messages_history = []
        for msg in conversation.messages.all():
            messages_history.append({
                'role': msg.role,
                'content': msg.content
            })

        # Générer la réponse
        result = ollama.chat(messages_history, model=model_name)

        if result['success']:
            ai_response = result['message'].get('content', '')

            # Sauvegarder la réponse de l'IA
            ChatMessage.objects.create(
                conversation=conversation,
                role='assistant',
                content=ai_response
            )

            # Mettre à jour la conversation
            conversation.save()  # Met à jour updated_at

            return JsonResponse({
                'success': True,
                'response': ai_response,
                'conversation_id': conversation.id
            })
        else:
            return JsonResponse({
                'success': False,
                'error': result.get('error', 'Erreur inconnue')
            })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


@login_required
@otp_required
@require_POST
def ai_chat_new_conversation(request):
    """Créer une nouvelle conversation"""

    try:
        data = json.loads(request.body)
        model_name = data.get('model', OllamaService().default_model)

        conversation = ChatConversation.objects.create(
            user=request.user,
            title="Nouvelle conversation",
            model_name=model_name
        )

        return JsonResponse({
            'success': True,
            'conversation_id': conversation.id
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


@login_required
@otp_required
@require_POST
def ai_chat_delete_conversation(request, conversation_id):
    """Supprimer une conversation"""

    try:
        conversation = get_object_or_404(ChatConversation, id=conversation_id, user=request.user)
        conversation.delete()

        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
