from django.urls import path
from HelloWorld.views import runoob

urlpatterns = [
    path('runoob/', runoob, name='runoob'),
]