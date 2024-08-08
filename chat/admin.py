from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Message

# Register the default User model with its default admin interface
admin.site.unregister(User)  # Unregister the default User model first
admin.site.register(User, DefaultUserAdmin)

# Register the Message model with a simple admin interface
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    readonly_fields = ('timestamp',)  # Make timestamp read-only in the admin interface
