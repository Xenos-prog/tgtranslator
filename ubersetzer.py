import os
import telebot
from deep_translator import GoogleTranslator
from langdetect import detect

TOKEN = os.environ["TOKEN"]

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "UA><DE übersetzer ist bereit.?\n"
        "Gib den Text für übersetzung"
    )
    
@bot.message_handler(func=lambda message:True)
def translate_text(message):
    text = message.text

    try:
        lang = detect(text)

        if lang== 'de' :
            translated = GoogleTranslator(
                source='de',
                target='uk'
            ).translate(text)

            bot.reply_to(
                message,
                f"UK: {translated}"
            )
        elif lang== 'uk' :
            translated = GoogleTranslator(
                source='uk',
                target='de'
            ).translate(text)

            bot.reply_to(
                message,
                f"DE: {translated}"
            )
        else:
            bot.reply_to(
                message,
                f"Kann man die sprache nicht finden"
                )
    
    except Exception as e:
        bot.reply_to(
        message,
        f"Something is wrong: \n {e}"
    )
print("Bot arbeitet...")
bot.infinity_polling()
