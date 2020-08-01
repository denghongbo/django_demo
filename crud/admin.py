from django.contrib import admin
from .models import Demo


class DemoAdmin(admin.ModelAdmin):
    list_display = ('username', 'age')
    search_fields = ('username', )

    list_filter = ('age', )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    class Media:
        js = ('js/hello.js', )


admin.site.register(Demo, DemoAdmin)
