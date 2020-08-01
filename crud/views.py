from django.http import JsonResponse
from .models import Demo


def index(request):
    demos = Demo.objects.all().values()[0:5]
    return JsonResponse(list(demos), safe=False)

