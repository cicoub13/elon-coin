import telegram
import credentials
from telegram.ext import Updater
from telegram.ext import CommandHandler

# Telegram Bot Auth
updater = Updater(token=credentials.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    f = open("chat_ids", "a")
    update.message.reply_text("Bienvenue. Vous seriez notifié(e) à chaque fois qu'Elon Musk tweet à propos de crypto-monnaie.")
    f.write(str(update.effective_chat.id))
    f.close()
    print("User {} added".format(str(update.effective_chat.id)))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
        