from django.urls import path
from . import views

urlpatterns = [
    path('procedure/', views.index, name='index')
]

