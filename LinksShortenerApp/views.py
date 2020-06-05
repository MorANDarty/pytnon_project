from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from LinksShortenerApp.models import get_analytics, get_url_for_redirect_by_hash, save_new_url, delete_all_links, \
    get_hash_by_url, update_click_count, delete_link


def home(request):
    if request.method == "POST":

        url = request.POST.get("url_field")
        print(url)
        if url is None:
            return render(request, "home_screen.html")

        else:
            save_new_url(url)
            return render(request, "home_screen.html",
                          {"hash_url": "/urls/" + get_hash_by_url(url)})

    else:
        return render(request, "home_screen.html")


def check_and_redirect(request, url_hash):
    url = get_url_for_redirect_by_hash(url_hash)
    if url is None:
        return HttpResponse("404 error, invalid hash link")

    else:
        update_click_count(url_hash)
        return HttpResponseRedirect(url)


def analytics(request):
    links = get_analytics()

    return render(request, "analytics_screen.html", {"links": links})


def delete_all(request):
    resp = delete_all_links()
    if resp is True:
        return HttpResponse("Success delete")
    else:
        return HttpResponse("Error on delete")


def delete_url(request, url_hash):
    if request.method == "POST":
        resp = delete_link(url_hash)
        if resp is True:
            return HttpResponseRedirect("/analytics")
        else:
            return HttpResponse("404 error, invalid hash link")
