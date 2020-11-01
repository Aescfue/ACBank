from telegram.ext import Updater, CommandHandler
import logging
import modelo

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Saludos, bienvenido al banco de la hermandad.")

def add(update, context):
    modelo.anadirCaja()
    
def list(update, context):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Saludos, bienvenido al banco de la hermandad.")

updater = Updater('token', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(filename='registros.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

