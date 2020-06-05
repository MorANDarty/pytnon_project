import string

import hashlib, uuid


def get_hash_url(url):
    salt = uuid.uuid4().hex
    hash_url = hashlib.sha256(str(url + salt).encode('utf-8')).hexdigest()
    if hash_url is None:
        print("hash url is None")
    else:
        print("hash url is not None")
        print(hash_url)
    return hash_url
