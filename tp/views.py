from django.shortcuts import render
from .models import Blog


def index(request):
    blogs = Blog.objects.all()[0:5]
    content = {
        'blogs': blogs
    }
    return render(request, 'tp/index.html', content)
