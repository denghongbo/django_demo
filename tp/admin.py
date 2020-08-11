from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'draft')


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('blog', )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
