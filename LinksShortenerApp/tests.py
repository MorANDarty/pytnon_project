from django.test import TestCase

# Create your tests here.
from LinksShortenerApp import models
from LinksShortenerApp.models import get_analytics, get_url_for_redirect_by_hash, save_new_url, delete_all_links, \
    get_hash_by_url, update_click_count, delete_link, Link
from LinksShortenerApp.utils.hash import get_hash_url

URL = "https://github.com"
HASH_URL = get_hash_url(URL)


class LinkTestCase(TestCase):

    def setUp(self):
        Link.objects.create(url=URL, hash_url=HASH_URL)

    def test_is_entity_created(self):
        self.assertEqual(models.is_have_that_link(HASH_URL), True)

    def test_save_func(self):
        self.assertEqual(save_new_url(URL), False)

    def test_counter_is_correct(self):
        models.update_click_count(HASH_URL)
        self.assertEqual(Link.objects.get(url=URL).click_count, 1)

    def test_that_hash_is_unique(self):
        hash_url = models.get_hash_by_url(URL)
        self.assertEqual(hash_url, HASH_URL)

    def test_entity_deleting(self):
        models.delete_link(HASH_URL)
        self.assertEqual(models.get_url_for_redirect_by_hash(HASH_URL), None)




