import random
import time
import telebot


# Задача 1. Создайте пользовательский аналог метода map()
def Map():
    def MAP(function1, numbers1):  
        return (function1(i) for i in numbers1)
    list_length1 = int(input("Input a length of a list: "))
    num_list1 = [random.randint(1, 10) for i in range(list_length1)]
    print(f"Original list is: {num_list1}")
    print(f"Finished list is: {list(MAP(lambda x: x**2 - 2, num_list1))}")
# Map()

# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.

def our_repeats(repeat_num):
    print(repeat_num, end = "")
    repeat_nums = int(input())
    def decorator(func):
        counts = 0
        love_is = func()
        while counts < repeat_nums:
            print(love_is)
            counts += 1
    return decorator

@our_repeats("Input numbers of function repeat: ")
def love():
    string1 = "I love puppies! "
    string2 = "I love ice cream! "
    string3 = "I love summer! "
    return (string1 + string2 + string3)

# Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import random
import telebot
import requests
import time

bot = telebot.TeleBot("6142085689:AAG5DQcUgKNyDOwjw4XWPM33UR840we7Dj8")
@bot.message_handler(content_types=['text'])
def greetings(message):
    # print(message)
    text = message.text
    if "привет" in text:
        bot.reply_to(message,f"Приветик, {message.from_user.first_name}. Если хочешь сыграть в игру, напиши мне 'игра'")
    if "игра" == text:
        game_start = bot.reply_to(message,"Я загадала число от 1 до 1000. Попробуй угадать. Для окончания игры скажи 'сдаюсь' :)")
        bot.register_next_step_handler(game_start, game)
        
num = int(random.randint(1, 1000))
print(num)

def game(message):
    repeats = 1
    if message.text == "сдаюсь":
            bot.reply_to(message, f"Ты не отгадал {repeats} раз, может, в следующем раунде получится :) А загадала я {num}")
    elif int(message.text) == num:
        bot.reply_to(message,f"Угадал! Всего за {repeats} попыток") 
    else:
        if int(message.text) > num:
            bot.reply_to(message,"Твое число больше")
            bot.register_next_step_handler(message, game)
        elif int(message.text) < num:
            bot.reply_to(message,"Твое число меньше")
            bot.register_next_step_handler(message, game)
    repeats = repeats + 1
bot.polling()
