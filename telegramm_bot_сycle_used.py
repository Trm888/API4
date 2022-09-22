import argparse
import os
import random
import time

import telegram
from environs import Env


def send_photos(time_sec, token, chat_id):
    bot = telegram.Bot(token=token)
    path_names = []
    for address, dirs, files in os.walk('image'):
        for file in files:
            with open(os.path.join(address, file), 'rb') as photo:
                bot.send_document(chat_id=chat_id, document=photo)
                path_names.append(os.path.join(address, file))
                time.sleep(time_sec)

    while True:
        with open(random.choice(path_names), 'rb') as random_photo:
            bot.send_document(chat_id=chat_id, document=random_photo)
            time.sleep(time_sec)


def main():
    env = Env()
    env.read_env()
    token = env.str("TELEGRAMM_TOKEN")
    chat_id = env.str("CHAT_ID")
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--time_sec', default=14400, help='время в секундах между пупбликациями')
    args = parser.parse_args()

    send_photos(int(args.time_sec), token, chat_id)


if __name__ == '__main__':
    main()
