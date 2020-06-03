import string

from hashids import Hashids
import hashlib, uuid
from django.urls import reverse

HASH_SALT = 'VyIZlWoq7VQCvJmq54gVHz5mb7GbaXdcT3Qz8dRssMyaYpTZl2ONBBnDA788Ef'
ALPHABET = string.ascii_lowercase

hashids = Hashids(salt=HASH_SALT, alphabet=ALPHABET)


def get_hash_url(url):
    salt = uuid.uuid4().hex
    url.encode('utf-8')
    hash_url = hashlib.sha256(str(url + salt).encode('utf-8')).hexdigest()
    if hash_url is None:
        print("hash url is None")
    else:
        print("hash url is not None")
        print(hash_url)
    return hash_url
