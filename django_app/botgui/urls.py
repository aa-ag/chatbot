############----------- IMPORTS -----------############
from django.contrib import admin
from django.urls import include, path


############----------- PATTERN(S) -----------############
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', include('bot.urls')),
]