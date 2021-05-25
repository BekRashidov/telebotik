# 😅😊👍🏻👌🏻👍🤛🏻🤜🏻😂🖕🏻😀😉👌😄😘😁☺️😔😭
import telebot

TOKEN = '1814628811:AAEAWu24ePcEBaZ5WqE9bIhDIIGnk0Z1yGE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Bizning saytimizga xush kelibsiz!😅')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Yordamga tayyormiz!')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello hello😅')
    elif message.text.lower() == 'xayr':
        bot.send_message(message.chat.id, 'Xayr kuningiz xayrli otsin!')
    elif message.text.lower() == 'oziz yaxshimi':
        bot.send_message(message.chat.id, 'Poxuy emasmi senga kotkalla!')


bot.polling()
