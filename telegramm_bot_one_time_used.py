import argparse
import os
import random

import telegram
from environs import Env


def send_photo(image_path, token, chat_id):
    bot = telegram.Bot(token=token)
    bot.send_document(chat_id=chat_id, document=open(image_path, 'rb'))


def main():
    env = Env()
    env.read_env()
    token = env.str("TELEGRAMM_TOKEN")
    chat_id = env.str("CHAT_ID")
    path_names = []
    for address, dirs, files in os.walk('image'):
        for name in files:
            path_names.append(os.path.join(address, name))
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--image_path', default=random.choice(path_names), help='время в секундах между пупбликациями')
    args = parser.parse_args()
    send_photo(args.image_path, token, chat_id)


if __name__ == '__main__':
    main()
