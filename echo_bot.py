import os
import self as self
import telebot
from flask import Flask, request



app = Flask(__name__)
TOKEN = "1864985053:AAG60rWPuy_b_KgXwyUpc3qXIFAOmyvMklw"
chat_id = "802134560"
bot = telebot.TeleBot(TOKEN)



users = {"id":"actions"}



@bot.message_handler(commands=['start'])
def send_welcome(message):
	photo = open('smart-2.png', 'rb')
	bot.reply_to(message, "Howdy, how are you doing?, im here to help you !"
						  " text /buy to see the new propertys in sell or if you are thinking"
							  "in make tourism in madrid /tourism to si or properties in rent"
							  "or /help if you have any hesitatation",photo)





@bot.message_handler(commands=['help'])
def send_welcome(message):
	markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
	markup.row("venta", "alquiler")
	markup.row("airB&B", "otros")
	bot.send_message(message.chat.id, "What do you need ?", reply_markup=markup)


@bot.message_handler(commands=['tourism'])
def send_welcome(message):
		bot.reply_to(message, "list of properties in Airb∞b?")

@bot.message_handler(self, commands=['buy'])
def send_welcome(message):
	parent_dir = os.getcwd()
	dir_name = "links.txt"
	path = os.path.join(parent_dir, dir_name)
	content = open(path, "r")
	lineas = content.readlines()
	bot.reply_to(message, f"mail, {lineas}")

def start_message(message):
	text_from_user = message.json["text"]
	pass

@bot.message_handler(func=lambda x: True)
def start_message(message):
	text_from_user = message.json["text"]
	id_from_user = message.json["id"]
	if "office" in text_from_user:
		bot.send_message(message.chat.id,f"Nuestra oficina se encuentra en Carretera de Canillas, 138, {message.chat.id}")
		bot.send_location(message.chat.id, "40.465297616884314", "-3.6397970886211115")
	elif "contacto" or "mail" in text_from_user:
		parent_dir = os.getcwd()
		dir_name = "mail.txt"
		path = os.path.join(parent_dir, dir_name)
		bot.send_message(message.id_from_user, "")
		content = open(path, "r")
		lineas = content.readlines()
		bot.send_message(id_from_user,f"mail, {lineas}")



@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot 26-05-2021", 200


@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://smartagency.herokuapp.com/' + TOKEN)
    return "Python Telegram Bot", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))