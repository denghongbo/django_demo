from django.urls import path
from . import views

app_name = 'tp'
urlpatterns = [
    path('', views.index, name='index')
]

