import telebot
from telebot import types

TOKEN = 'token here'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum {0.first_name} {0.last_name}!\n Asaxiy.uz saytining telegram botiga xush kelibsiz!".format(message.from_user, bot.get_me()), parse_mode='html')
    photo = open('tmp/asaxiy.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['kataloglar'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Kitoblar', callback_data='kitoblar')
    item1 = types.InlineKeyboardButton('Elektronika', callback_data='electronika')
    item2 = types.InlineKeyboardButton('Uy Jihozlari', callback_data='uy_jihozlar')
    item3 = types.InlineKeyboardButton('Gadjetlar', callback_data='gadjetlar')
    item4 = types.InlineKeyboardButton('Sport ashyolar', callback_data='sport_ashyolar')
    web = types.InlineKeyboardButton('Web sahifa', url='https://asaxiy.uz/')
    markup.add(item, item1,item2,item3,item4, web)
    bot.send_message(message.chat.id, 'Quyidagilardan birini tanlang', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def data(call):
    if call.message:
        if call.data == 'kitoblar':
            bot.send_message(call.message.chat.id, 'No data yet')
        elif call.data == 'elektronika':
            bot.send_message(call.message.chat.id, 'No data yet1')
        elif call.data == 'uy_jihozlar':
            bot.send_message(call.message.chat.id, 'No data yet2')
        elif call.data == 'gadjetlar':
            bot.send_message(call.message.chat.id, 'No data yet3')
        elif call.data == 'sport_ashyolar':
            bot.send_message(call.message.chat.id, 'No data yet4')



bot.polling()
