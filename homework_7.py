import random
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

bot = telebot.TeleBot("6142085689:AAG5DQcUgKNyDOwjw4XWPM33UR840we7Dj8")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    text = message.text
    if  text == "game":
        game_start = bot.reply_to(message,"I picked a number from 1 to 1000. Try to guess. To finish, write 'give up':)")
        bot.register_next_step_handler(game_start, letsplay)


num = int(random.randint(1, 1000))
print(num)
counter = 0
def letsplay(message):
    global num
    global counter
    if message.text.isdigit() == True:
        if int(message.text) == num:
            counter += 1
            bot.reply_to(message,f"Сongratulations, you guessed right! You made {counter} tries :)") 
        else:
            if int(message.text) > num:
                counter += 1
                bot.reply_to(message,"Your number is higher")
                bot.register_next_step_handler(message, letsplay)
            elif int(message.text) < num:
                counter += 1
                bot.reply_to(message,"Your number is less")
                bot.register_next_step_handler(message, letsplay)
    elif message.text == "give up":
            bot.reply_to(message, f"You made {counter} tries. Maybe you'll win the next round :) And my number was {num}")
    else:
        bot.reply_to(message,"Oops, you inputted something wrong o_O. Please, try again")
        bot.register_next_step_handler(message, letsplay)

bot.polling()