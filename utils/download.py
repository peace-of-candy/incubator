import os
from os.path import dirname, abspath

import requests


DOWNLOAD_PATH = dirname(dirname(abspath(__file__))) + "/download/"

def file_exists(path: str) -> bool:
    """
    :param path: can be either a filename or a directory name
    """
    return os.path.exists(path)


def get_data(url):
    filename = "".join([c for c in url if c.isalpha() or c.isdigit() or c == ' ']).rstrip()
    filename += ".data"
    if len(filename) > 254:
        filename = filename[-254:]
    filename = DOWNLOAD_PATH + filename
    if not file_exists(filename):
        os.makedirs(DOWNLOAD_PATH, exist_ok=True)
        with open(filename, 'w') as f:
            f.write(requests.get(url).text)

    data = open(filename).read()
    return data


def get_html(url):
    return get_data(url)
