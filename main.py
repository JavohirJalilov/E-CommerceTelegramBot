from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    first_name = update.effective_user.first_name
    
    text = f'Assalomu alaykum {first_name} elektron tijorat botiga hush kelibsiz !'
    button1 = KeyboardButton('π Maxsulotlar')
    button2 = KeyboardButton('π Savatcha')
    button3 = KeyboardButton('π¦ Buyurtmalarim')
    button4 = KeyboardButton('π¨ Profilβ')
    button5 = KeyboardButton('π Yordam')

    reply_markup = ReplyKeyboardMarkup(
        [
            [button1,button2],
            [button3,button4,button5]
        ],resize_keyboard=True
    )
    update.message.reply_text(text = text,reply_markup=reply_markup)
    
updater = Updater('1680699486:AAEFcJeNqOvxAjPjTnkx2FgUwCf_W9NdsOE')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()