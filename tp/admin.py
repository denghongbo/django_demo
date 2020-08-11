from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'draft')


admin.site.register(Blog, BlogAdmin)
