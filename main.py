import telegram,os,env_var,functions
from telegram import Update
from functions import *
from telegram.ext import CommandHandler,Updater

# defining some vars
my_token=os.getenv('TOKEN')
bot= telegram.Bot(token=my_token)
# updater receives updates from tele and sends it to the dispatcher
updater= Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher

# Command handler deals with commands which are essentially messages that starts with '/'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()