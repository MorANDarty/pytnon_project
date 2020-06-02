from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World!")


def check_and_redirect(request, url_hash):
    return HttpResponse('U are try to go /'+str(url_hash))



