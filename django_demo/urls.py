"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "管理系统"
admin.site.site_title = "管理系统"
admin.site.site_url = "localhost:8000"
admin.site.index_title = None
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('crud/', include('crud.urls')),
    path('device-data/', include('device_data.urls')),
    path('', include('index.urls')),
    path('', include('ajax_select.urls')),
    path('tb/', include('tb.urls')),
    path('tp/', include('tp.urls')),
]
