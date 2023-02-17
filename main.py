# using the pyTelegramBotAPI

# for token
import os

# for chatbot 
import telebot

# import telegram token from secrets
bot = telebot.TeleBot(os.environ['TOKEN'])

print('Hello Mendi')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#   bot.reply_to(message, message.text)


# create two buttons for the bot
@bot.message_handler(func=lambda message: True)
def echo_all_buttons(message):
  bot.reply_to(message, "I'm a bot, and I can do this:")


print("Bot Live!")
bot.polling()
