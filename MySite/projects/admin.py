from django.contrib import admin
from projects.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Сообщения"""
    list_display = ('name', 'email', 'subject',)
