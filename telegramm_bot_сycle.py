import argparse
import os
import random
import time

import telegram
from environs import Env


# bot.send_message(chat_id='@alis_devman', text="I'm sorry Dave I'm afraid I can't do that.")
#
# bot.send_document(chat_id='@alis_devman', document=open('image/NASA_EPIC_3.png', 'rb'))

# images_name = os.walk("image")
# for i in images_name:
#     print(i)

# while True:
def photo_send(time_sec, token):
    bot = telegram.Bot(token=token)
    path_name = []
    for address, dirs, files in os.walk('image'):
        for name in files:
            bot.send_document(chat_id='@alis_devman', document=open(os.path.join(address, name), 'rb'))
            path_name.append(os.path.join(address, name))
            time.sleep(time_sec)

    while True:
        bot.send_document(chat_id='@alis_devman', document=open(random.choice(path_name), 'rb'))
        time.sleep(time_sec)


def main():
    env = Env()
    env.read_env()
    token = env.str("TELEGRAMM_TOKEN")
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--time_sec', default=14400, help='время в секундах между пупбликациями')
    args = parser.parse_args()

    photo_send(int(args.time_sec), token)


if __name__ == '__main__':
    main()
