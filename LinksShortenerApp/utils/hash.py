import string

from hashids import Hashids
from django.urls import reverse

HASH_SALT = 'VyIZlWoq7VQCvJmq54gVHz5mb7GbaXdcT3Qz8dRssMyaYpTZl2ONBBnDA788Ef'
ALPHABET = string.ascii_lowercase

hashids = Hashids(salt=HASH_SALT, alphabet=ALPHABET)


def get_hash_url(url):
    hash_url = hashids.encode(url)
    print(hash_url)
    return hashids.encode(url)
