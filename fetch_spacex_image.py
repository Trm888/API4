import argparse
import os
from pathlib import Path

import requests
from environs import Env

from download_image import download_image


def download_spacex_flight_images(id):
    api_url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(api_url)
    response.raise_for_status()
    for link_number, link in enumerate(response.json()["links"]['flickr']['original']):
        filepath = Path(os.getcwd(), 'image', f'spacex{link_number}.jpg')
        download_image(link, filepath)


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--id', default='latest', help='Id полета')
    args = parser.parse_args()
    Path(os.getcwd(), 'image').mkdir(parents=True, exist_ok=True)
    download_spacex_flight_images(args.id)


if __name__ == '__main__':
    main()

