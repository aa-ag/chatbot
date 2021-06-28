############----------- IMPORTS -----------############
from django.urls import path
from . import views


############----------- PATTERN(S) -----------############
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room_name>/', views.room, name='room'),
]