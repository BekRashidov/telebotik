from bs4 import BeautifulSoup
import requests
import telebot

TOKEN = '1814628811:AAEAWu24ePcEBaZ5WqE9bIhDIIGnk0Z1yGE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id, 'Salom /obhavo komandasini kirgizing')

@bot.message_handler(commands='obhavo')
def weather(message):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    resp = requests.get('https://www.gismeteo.com/weather-dzhumabazar-323078/', headers=headers).text
    soup = BeautifulSoup(resp, 'html.parser')

    #find
    title = soup.find('span', class_='tab-weather__value_l')
    bot.send_message(message.chat.id, ' Xarromi Molbozorda ob havo:')
    bot.send_message(message.chat.id, title.get_text())

bot.polling()