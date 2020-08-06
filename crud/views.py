from django.http import HttpResponse, Http404, JsonResponse
from .models import Demo, Person


def index(request):

    try:
        p = Person.objects.get(pk=1)
        return HttpResponse(p.get_shirt_size_display())
    except Person.DoesNotExist:
        raise Http404("person does not found")


def create(request):
    p = Person(name="ZhangDaBao", shirt_size='M')
    p.save()
    return HttpResponse(p.id)
