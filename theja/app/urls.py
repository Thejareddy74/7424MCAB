from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('green/',views.green,name='green'),
    path('displaygreen/',views.displaygreen,name='displaygreen'),
]