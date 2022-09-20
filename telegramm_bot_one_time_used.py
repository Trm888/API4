import argparse
import os
import random

import telegram
from environs import Env


def photo_send(image_path, token):
    bot = telegram.Bot(token=token)
    bot.send_document(chat_id='@alis_devman', document=open(image_path, 'rb'))


def main():
    env = Env()
    env.read_env()
    token = env.str("TELEGRAMM_TOKEN")
    path_name = []
    for address, dirs, files in os.walk('image'):
        for name in files:
            path_name.append(os.path.join(address, name))
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--image_path', default=random.choice(path_name), help='время в секундах между пупбликациями')
    args = parser.parse_args()
    photo_send(args.image_path, token)


if __name__ == '__main__':
    main()