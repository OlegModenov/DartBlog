from django.urls import path
from .views import index  # импортируем наше представление

urlpatterns = [
    path('', index),
]