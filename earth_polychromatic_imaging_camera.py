import datetime
import os
from pathlib import Path

import requests
from environs import Env

from extract_extension import extract_extension


def download_earth_polychromatic_images(token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': token}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    for index in range(len(decoded_response)):
        image_date = datetime.date.fromisoformat(decoded_response[index]['date'][:10])
        image_response = requests.get(
            f'https://epic.gsfc.nasa.gov/archive/natural/{image_date.year}/{image_date.month:02d}/'
            f'{image_date.day:02d}/png/{decoded_response[index]["image"]}.png',
            params=params)
        extension = extract_extension(image_response.url)
        filepath = Path(os.getcwd(), 'image', f'NASA_EPIC_{index}{extension}')
        with open(filepath, 'wb') as file:
            file.write(image_response.content)


def main():
    env = Env()
    env.read_env()
    token = env.str("NASA_TOKEN")
    Path(os.getcwd(), 'image').mkdir(parents=True, exist_ok=True)

    download_earth_polychromatic_images(token)


if __name__ == '__main__':
    main()

