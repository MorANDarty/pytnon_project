from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from LinksShortenerApp.models import get_analytics, get_url_for_redirect_by_hash, save_new_url, delete_all_links
from LinksShortenerApp.utils.hash import get_hash_url


def home(request):
    return render(request, "home_screen.html")


def check_and_redirect(request, url_hash):
    url = get_url_for_redirect_by_hash(url_hash)
    if url is None:
        return HttpResponse("404 error, invalid hash link")
    else:

        return HttpResponseRedirect(url)


def analytics(request):
    links = get_analytics()
    return render(request, "analytics_screen.html", {"links": links})


def create_url_hash(request):
    url = request.POST.get("url_field")
    print(url)
    if url is None:
        return render(request, "home_screen.html")
    else:
        resp_from_db = save_new_url(url)
        if resp_from_db is True:
            return render(request, "home_screen.html", {"hash_url": request.get_host() + "/urls/" + get_hash_url(url)})
        else:
            return render(request, "home_screen.html", {"hash_url": request.get_host() + "/urls/" + get_hash_url(url)})


def delete_all(request):
    resp = delete_all_links()
    if resp is True:
        return HttpResponse("Success delete")
    else:
        return HttpResponse("Error on delete")
