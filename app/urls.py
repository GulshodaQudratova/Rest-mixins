from django.urls import path
from .views import *
urlpatterns = [
    path('',TelegramUserList.as_view()),
    # path('<int:pk>',TelegramUserDetail.as_view())
]
