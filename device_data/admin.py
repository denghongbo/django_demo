from django.contrib import admin
from .models import UserData
from django.contrib.auth.models import User


class UserDataAdmin(admin.ModelAdmin):

    list_display = ('uid', 'data_key', 'data_val', 'data_key_val')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


admin.site.register(UserData, UserDataAdmin)
