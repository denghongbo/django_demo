from django.urls import path
from . import views

app_name = 'tb'
urlpatterns = [
    path('index/', views.index, name='index')
]