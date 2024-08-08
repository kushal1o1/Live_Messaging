from django.contrib import admin
from .models import User, Message

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'content', 'timestamp']
    list_filter = ['sender', 'receiver']
    search_fields = ['content']
