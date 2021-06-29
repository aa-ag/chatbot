############----------- IMPORTS -----------############
from django.urls import path
from . import views


############----------- PATTERN(S) -----------############
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]