from telegram.ext import Updater, CommandHandler
import requests, re
from send_message import bop

updater = Updater('910018291:AAEXiRAqr-EZnJp-k_Xo1d5al1yhxskG5yw')
dp = updater.dispatcher
dp.add_handler(CommandHandler('bop',bop))
updater.start_polling()
updater.idle()



def get_url():
    '''
    Get an url of a random image of a dog 
    '''
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
