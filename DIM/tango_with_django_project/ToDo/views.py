
from django.http import HttpResponse

def index(request):
    return HttpResponse("ToDo says hello world!")