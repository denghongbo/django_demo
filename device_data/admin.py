from django.contrib import admin
from .models import UserData


class UserDataAdmin(admin.ModelAdmin):

    list_display = ('uid', 'data_key', 'data_val', 'data_key_val')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(uid_id=2)


admin.site.register(UserData, UserDataAdmin)
