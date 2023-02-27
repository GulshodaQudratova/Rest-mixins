from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    telegram_id = models.IntegerField(unique=True)
    language = models.CharField(max_length=5,default='uz')
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name