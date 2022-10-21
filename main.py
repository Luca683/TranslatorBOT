from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import googletrans
from googletrans import Translator

TOKEN = open("config/token.config.dist", "r").read().strip()

def start(update, context):
    update.message.reply_text("Ciao! Digita una frase e io la tradurrò per te.")

def reply(update, context):
    text = update.message.text.lower()

    translator = Translator()
    #translate_text = 
    update.message.reply_text(translator.translate(text, src='it', dest='en').text)

    #update.message.reply_text(translate_text)
   
updater = Updater(TOKEN) #La classe updater ci permette di controllare il nostro bot, quindi gli passiamo il TOKEN relativo
updater.dispatcher.add_handler(CommandHandler("start", start)) #Quando il bot riceve il comando start allora la funzione "start" deve gestirlo
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply)) #Stesso concetto per i messaggi mandati da noi sul bot

print("bot in ascolto ...")
updater.start_polling() #Per mantenere sempre il bot in ascolto