import telebot
from telebot import types


bot = telebot.TeleBot("6142085689:AAG5DQcUgKNyDOwjw4XWPM33UR840we7Dj8")
markup = types.ReplyKeyboardMarkup(row_width = 1)
btn_reg = types.KeyboardButton('регистрация')
btn_alarm = types.KeyboardButton('оповещение')
markup.add(btn_reg, btn_alarm)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Howdy", reply_markup = markup)

@bot.message_handler(content_types=['text'])
def text_messange(message):
    data = open("log.txt", mode = "a", encoding = "utf-8")
    text = (f"{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n")
    data.write(text)
    data.close()
    if message.text == "регистрация":
        data = open("registred_user.txt", mode = "r", encoding = "utf-8")
        id_list = data.readlines()
        data.close()
        id_list = list(el[:-1] for el in id_list)
        if str(message.from_user.id) not in id_list:
            data = open("registred_user.txt", mode = "a", encoding = "utf-8")
            data.write(f"{message.from_user.id}\n")
            data.close()
            bot.reply_to(message, "Регистарация прошла успешла!")
        else:
            bot.reply_to(message, "Вы уже зарегистрированы!")
    elif message.text == "оповещение":
        data = open("registred_user.txt", mode = "r", encoding = "utf-8")
        id_list = data.read().split('\n')
        data.close()
        id_list = id_list[:-1]
        for id in id_list:
            bot.send_message(id, "Совещание через 5 минут!")
bot.polling()