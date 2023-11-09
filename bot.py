import requests
import telebot

token = "6758988489:AAHXRcWElqb-FQyPsKcKirSkIXazCPu3lU4"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(msg):
	bot.reply_to(msg,'ارسل اسمك')

@bot.message_handler(content_types=['text'])
def ph(msg):
	name = msg.text
	url = "https://www.brandcrowd.com/maker/logos?text="+name
	req = requests.get(url).text
	for i in range(11,23):
		logo = req.split("img src=\"")[i].split('"')[0].replace("amp;","")
		bot.send_photo(msg.chat.id,logo)

bot.polling()
