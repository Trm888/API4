import os
from pathlib import Path

import requests
from environs import Env

from download_image import download_image
from extract_extension import extract_extension


def download_astronomy_picture_day(token):
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token,
              'count': 40,
              'thumbs': True}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    serialized_response = response.json()
    for index in range(len(serialized_response)):
        extension = extract_extension(serialized_response[index]["url"])
        if extension:
            filename = Path(os.getcwd(), 'image', f'NASA_APOD_{str(index)}{extension}')
            download_image(serialized_response[index]['url'], filename)


def main():
    env = Env()
    env.read_env()
    token = env.str("NASA_TOKEN")
    Path(os.getcwd(), 'image').mkdir(parents=True, exist_ok=True)
    download_astronomy_picture_day(token)

if __name__ == '__main__':
    main()
