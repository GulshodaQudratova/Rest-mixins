from django.contrib import admin

# Register your models here.
from .models import TelegramUser
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['name' , 'telegram_id' , 'language' , 'added']