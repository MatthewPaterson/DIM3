from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': " BLAH BLAH BLAH"}

    return render_to_response('rango/index.html', context_dict,context)