from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googletrans import Translator

TOKEN = open("config/token.config.dist", "r").read().strip()

def start(update, context):
    update.message.reply_text("Ciao! Digita una frase e io la tradurrò per te.")

def reply(update, context):
    text = update.message.text.lower()

    translator = Translator()
    update.message.reply_text(translator.translate(text, src='it', dest='en').text)
   
updater = Updater(TOKEN) 
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))

print("bot in ascolto ...")
updater.start_polling()