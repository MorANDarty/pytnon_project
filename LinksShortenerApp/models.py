from django.db import models

# Create your models here.
from django.db.models import F

from LinksShortenerApp.utils.hash import get_hash_url


class Link(models.Model):
    url = models.URLField(max_length=2083)
    hash_url = models.CharField(max_length=16)
    click_count = models.PositiveIntegerField(default=0)


def get_analytics():
    return Link.objects.all().order_by('-click_count')


def is_have_that_link(hash_url):
    try:
        link = Link.objects.get(hash_url=hash_url)
    except Link.DoesNotExist:
        link = None

    if link is None:
        return False
    else:
        return True


def get_url_for_redirect_by_hash(hash_url):
    if is_have_that_link(hash_url) is True:
        return Link.objects.get(hash_url=hash_url).url
    else:
        return None


def get_hash_by_url(url):
    try:
        link = Link.objects.get(url=url)
    except Link.DoesNotExist:
        link = None

    if link is None:
        return None
    else:
        return link.hash_url


def save_new_url(url):
    try:
        link = Link.objects.get(url=url)
    except Link.DoesNotExist:
        link = None
    if link is None:
        Link.objects.create(url=url, hash_url=get_hash_url(url))
        return True
    else:
        return False


def update_click_count(hash_url):
    if is_have_that_link(hash_url) is True:
        Link.objects.all().filter(hash_url=hash_url).update(click_count=F("click_count") + 1)
        return True
    else:
        return False


def delete_link(hash_url):
    if is_have_that_link(hash_url) is True:
        Link.objects.filter(hash_url=hash_url).delete()
        return True
    else:
        return False


def delete_all_links():
    try:
        Link.objects.all().delete()
        return True
    except Link.DoesNotExist:
        return False
