from django.contrib import admin
from .models import UserProfile, LoginAttempt, ChatConversation, ChatMessage


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'two_fa_enabled', 'phone_number', 'created_at']
    list_filter = ['two_fa_enabled', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone_number']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Utilisateur', {
            'fields': ('user',)
        }),
        ('Configuration 2FA', {
            'fields': ('two_fa_enabled', 'phone_number')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(LoginAttempt)
class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ['username', 'user', 'success', 'two_fa_completed', 'ip_address', 'timestamp']
    list_filter = ['success', 'two_fa_completed', 'timestamp']
    search_fields = ['username', 'user__username', 'ip_address']
    readonly_fields = ['user', 'username', 'ip_address', 'success', 'two_fa_completed',
                       'timestamp', 'user_agent']
    date_hierarchy = 'timestamp'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 0
    readonly_fields = ['role', 'content', 'timestamp']
    can_delete = False


@admin.register(ChatConversation)
class ChatConversationAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'model_name', 'created_at', 'updated_at']
    list_filter = ['model_name', 'created_at']
    search_fields = ['user__username', 'title']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ChatMessageInline]


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['conversation', 'role', 'content_preview', 'timestamp']
    list_filter = ['role', 'timestamp']
    search_fields = ['content', 'conversation__title']
    readonly_fields = ['conversation', 'role', 'content', 'timestamp']

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Contenu'

    def has_add_permission(self, request):
        return False
