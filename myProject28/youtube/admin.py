from django.contrib import admin
from .models import YouTubeUser
from django.core.cache import cache
from django.contrib import messages

@admin.action(description='Clear users cache')
def clear_users_cache(modeladmin, request, queryset):
    cache.delete('users_data')
    messages.success(request, 'Users cache cleared')

@admin.register(YouTubeUser)
class YouTubeUserAdmin(admin.ModelAdmin):
    list_display=('name','email','subscribers')
    actions=[clear_users_cache]
# Register your models here.
