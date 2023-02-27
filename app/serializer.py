from rest_framework import serializers
from .models import *
class TelegramUserSerializer(serializers.ModelSerializer):
    model = TelegramUser
    fields = '__all__'