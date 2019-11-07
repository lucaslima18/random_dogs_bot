from telegram.ext import Updater, CommandHandler
from send_message import bop

updater = Updater('910018291:AAEXiRAqr-EZnJp-k_Xo1d5al1yhxskG5yw')
dp = updater.dispatcher
dp.add_handler(CommandHandler('bop',bop))
updater.start_polling()
updater.idle()