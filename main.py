import key as K
from telegram.ext import *
import Responses as R

print("Bot says hi")

def start(update, context):
    update.message.reply_text('Started')

def help(update, context):
    update.message.reply_text("I cannot help")

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    update.message.reply_text(text_caps)

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater= Updater(K.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("caps", caps))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(5)

main()
