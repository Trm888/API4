import requests


def download_images(url, path):
    headers = {'User-Agent': ''}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
