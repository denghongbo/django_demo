from django.http import HttpResponse
from django.core import serializers


def index(request):
    data = 'todo'
    return HttpResponse(data)

