import datetime
import os
from pathlib import Path

import requests
from environs import Env

from extract_extension import extract_extension


def earth_polychromatic_imaging_camera(token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': token}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    for index in range(len(response.json())):
        image_date = datetime.date.fromisoformat(response.json()[index]['date'][:10])
        image_response = requests.get(
            f'https://epic.gsfc.nasa.gov/archive/natural/{image_date.year}/{image_date.month:02d}/'
            f'{image_date.day:02d}/png/{response.json()[index]["image"]}.png',
            params=params)
        filename = f'image/NASA_EPIC_{str(index)}{extract_extension(image_response.url)}'
        with open(filename, 'wb') as file:
            file.write(image_response.content)

def main():
    env = Env()
    env.read_env()
    token = env.str("NASA_TOKEN")
    Path(os.getcwd() + '/image').mkdir(parents=True, exist_ok=True)

    earth_polychromatic_imaging_camera(token)

if __name__ == '__main__':
    main()