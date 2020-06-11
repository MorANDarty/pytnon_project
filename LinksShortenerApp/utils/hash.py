import string

import hashlib

SALT = "dkfj34fjfd949rwf9f39ff9ef2092jfd"

def get_hash_url(url):
    hash_url = hashlib.sha256(str(url + SALT).encode('utf-8')).hexdigest()
    if hash_url is None:
        print("hash url is None")
    else:
        print("hash url is not None")
        print(hash_url)
    return hash_url
