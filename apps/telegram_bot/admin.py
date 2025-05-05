from django.contrib import admin

from apps.telegram_bot.models import TelegramUser
# Register your models here.

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')