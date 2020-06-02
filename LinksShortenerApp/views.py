from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, "home_screen.html")


def check_and_redirect(request, url_hash):
    if url_hash == "vk":
        return HttpResponseRedirect("https://vk.com")
    return HttpResponse('U are try to go /' + str(url_hash))


def analytics(request):
    return render(request, "analytics_screen.html")