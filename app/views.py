# from django.shortcuts import render
# from .models import * 
# from .serializer import *
# from rest_framework.generics import *
# from rest_framework.mixins import *
# class TelegramUserList(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = TelegramUser.objects.all()
#     serializer_class = TeleramUserSerializer
#     print(queryset)
#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args, **kwargs)
    # def post(self,request,*args, **kwargs):
    #     return self.create(request,*args, **kwargs)
# class TelegramUserDetail(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
#     queryset = TelegramUser.objects.all()
#     serializer_class = TeleramUserSerializer
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)
#     def put(self,request,*args, **kwargs):
#         return self.update(request,*args, **kwargs)
#     def patch(self,request,*args, **kwargs):
#         return self.partial_update(request,*args, **kwargs)
#     def delete(self,request,*args, **kwargs):
#         return self.destroy(request,*args, **kwargs)

from django.shortcuts import render

# Create your views here.
from .serializer import *
from .models import *
from rest_framework.generics import *
from rest_framework.mixins import *
class TelegramUserList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = TelegramUser.objects.all()
    serializer_class =  TelegramUserSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class TelegramUserDetail(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset = TelegramUser.objects.all()
    serializer_class =  TelegramUserSerializer
    # lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
       