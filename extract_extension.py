import os
from urllib.parse import urlparse, unquote


def extract_extension(url):
    url_path = urlparse(url).path
    return os.path.splitext(unquote(url_path, encoding='utf-8', errors='replace'))[1]


