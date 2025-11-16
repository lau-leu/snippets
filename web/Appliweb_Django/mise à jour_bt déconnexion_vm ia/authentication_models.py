from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Profil utilisateur avec informations 2FA"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # Contact pour 2FA
    phone_number = models.CharField(max_length=20, blank=True, null=True,
                                   help_text="Format: +33612345678")

    # Activation 2FA
    two_fa_enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profil utilisateur"
        verbose_name_plural = "Profils utilisateurs"

    def __str__(self):
        return f"Profil de {self.user.username}"


class LoginAttempt(models.Model):
    """Historique des tentatives de connexion"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=150)
    ip_address = models.GenericIPAddressField()
    success = models.BooleanField(default=False)
    two_fa_completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tentative de connexion"
        verbose_name_plural = "Tentatives de connexion"
        ordering = ['-timestamp']

    def __str__(self):
        status = "Réussie" if self.success else "Échouée"
        return f"{self.username} - {status} - {self.timestamp}"


class ChatConversation(models.Model):
    """Conversation de chat avec l'IA"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    title = models.CharField(max_length=200, default="Nouvelle conversation")
    model_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Conversation"
        verbose_name_plural = "Conversations"
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class ChatMessage(models.Model):
    """Message dans une conversation"""

    ROLE_CHOICES = [
        ('user', 'Utilisateur'),
        ('assistant', 'Assistant'),
    ]

    conversation = models.ForeignKey(ChatConversation, on_delete=models.CASCADE,
                                    related_name='messages')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.role}: {self.content[:50]}"
