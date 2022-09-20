import os
from pathlib import Path

import requests
from environs import Env

from download_image import download_images
from extract_extension import extract_extension


def astronomy_picture_of_the_day(token):
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token,
              'count': 30,
              'thumbs': True}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    for index in range(len(response.json())):
        filename = f'image/NASA_APOD_{str(index)}' \
                   f'{extract_extension(response.json()[index]["url"])}'
        download_images(response.json()[index]['url'], filename)


def main():
    env = Env()
    env.read_env()
    token = env.str("NASA_TOKEN")
    Path(os.getcwd() + '/image').mkdir(parents=True, exist_ok=True)

    astronomy_picture_of_the_day(token)

if __name__ == '__main__':
    main()
