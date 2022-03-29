import telebot
from io import StringIO
from contextlib import redirect_stdout

bot = telebot.TeleBot("5249096188:AAHsBY0JA0MbpTZ3WgHTLuRAKv0fY6wUYdg")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    f = StringIO()
	q = "secret"
    with redirect_stdout(f):
        exec(message.text)
    bot.reply_to(message, f.getvalue())


bot.infinity_polling()
