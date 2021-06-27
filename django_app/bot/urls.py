############----------- IMPORTS -----------############
from django.urls import path
from . import views


############----------- PATTERN(S) -----------############
urlpatterns = [
    path('', views.home, name='home'),
]