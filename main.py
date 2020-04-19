from telegram.ext import Updater, CommandHandler
import requests, re
from send_message import bop


def get_url():
    '''
    Get an url of a random image of a dog 
    '''
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
updater = Updater('910018291:AAEXiRAqr-EZnJp-k_Xo1d5al1yhxskG5yw')
dp = updater.dispatcher
dp.add_handler(CommandHandler('bop',bop))
updater.start_polling()
updater.idle()
