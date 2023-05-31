# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
import telebot

# bot = telebot.TeleBot("")
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.from_user.id, "Howdy")

# @bot.message_handler(content_types=['text'])
# def text_messange(message):
#     data1 = open("log1.txt", mode = "a", encoding = "utf-8")
#     text1 = (f"{message.from_user.id}: {message.text}\n")
#     data1.write(text1)
#     data1.close()
# bot.polling()



# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.

bot = telebot.TeleBot(":")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Howdy")

@bot.message_handler(content_types=['text'])
def text_messange(message):
    data2 = open("log2.txt", mode = "a", encoding = "utf-8")
    text2 = (f"{message.from_user.id}: {message.text}\n")
    data2.write(text2)
    data2.close()
    if "?" in text2:
        question = text2.split(":")[1]
        print(f"Question of user: {question}")
        id = (text2.split(":"))[0]
        answer = input("Input answer: ")
        bot.send_message(id, answer)
    else:
        bot.send_message(message.from_user.id, "Please, ask your question")
bot.polling()