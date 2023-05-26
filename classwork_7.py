# TASK1

def our_format(func):
    def decorator(*args):
        for arg in args:
            print(f"{arg} +", end = " ")
        print("\b\b=", end = " ")

        func(*args)
    return decorator

@our_format
def sum(a, b):
    print(a + b)

@our_format
def sum4(a, b, c, d):
    print(a + b + c + d)

# sum(4, 6)
# sum4(4, 2, 1, 9)

# TASK2

def greetings(hello):
    def our_greetings(func):
        def decorator():
            name = func()
            print(f"{hello}, {name}")
        return decorator
    return our_greetings

@greetings("Приветик")
def get_name():
    return input("Как тебя зовут?\n")
# get_name()



# TASK3
import telebot
import requests
import time


bot = telebot.TeleBot("6142085689:AAG5DQcUgKNyDOwjw4XWPM33UR840we7Dj8")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
        
@bot.message_handler(content_types=['text'])
def greetings(message):
    # print(message)
    text = message.text
    if "привет" in text:
        bot.reply_to(message,f"Приветик, {message.from_user.first_name}")
    elif text == "погода":
        req = requests.get("https://wttr.in/?0T")
        bot.reply_to(message, req.text)
    elif text == "собачка":
        req = requests.get(f'https://cataas.com/cat?{time.time()}')
        bot.send_photo(message.from_user.id, req.content)
bot.polling()