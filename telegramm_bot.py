import telegram

TOKEN = '5797612641:AAF9xfQ1LCrbrlY77xP-sbvzvil_P5CRynE'

bot = telegram.Bot(token=TOKEN)

print(bot.get_me())

bot.send_message(chat_id='@alis_devman', text="I'm sorry Dave I'm afraid I can't do that.")