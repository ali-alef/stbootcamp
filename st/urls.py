from django.urls import path, include
from . import views

urlpatterns = [
    path('apply/', views.apply),
]
