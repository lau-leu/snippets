from django.urls import path
from . import views

urlpatterns = [
    path('setup-2fa/', views.setup_2fa_choice, name='setup_2fa_choice'),
    path('hello/', views.hello_view, name='hello'),
    path('logout/', views.logout_view, name='logout'),

    # Chat IA
    path('ai-chat/', views.ai_chat_view, name='ai_chat'),
    path('ai-chat/send/', views.ai_chat_send, name='ai_chat_send'),
    path('ai-chat/new/', views.ai_chat_new_conversation, name='ai_chat_new'),
    path('ai-chat/delete/<int:conversation_id>/', views.ai_chat_delete_conversation, name='ai_chat_delete'),
]
