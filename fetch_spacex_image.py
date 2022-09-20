import argparse
import os
from pathlib import Path

import requests
from environs import Env

from download_image import download_images


def fetch_spacex_image(id):
    api_url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(api_url)
    response.raise_for_status()
    for link_number, link in enumerate(response.json()["links"]['flickr']['original']):
        filename = 'image/spacex' + str(link_number) + '.jpg'
        download_images(link, filename)


def main():
    env = Env()
    env.read_env()
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--id', default='latest', help='Id полета')
    args = parser.parse_args()
    Path(os.getcwd() + '/image').mkdir(parents=True, exist_ok=True)
    fetch_spacex_image(args.id)


if __name__ == '__main__':
    main()
