# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.

def Fibonacci():
    number_el = int (input("Input a number: "))
    previous_num_1 = 0
    previous_num_2 = 1

    Fibonacci_sequence = []
    for index in range(number_el):
        Fibonacci_sequence.append(previous_num_1)
        num = previous_num_1 + previous_num_2
        previous_num_1 = previous_num_2
        previous_num_2 = num
    print(Fibonacci_sequence) 

#Fibonacci()

# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву. Список фруктов заполните вручную.

def Fruits():
    fruit_basket = ("apple", "avocado", "apricot", "banana", "date", "fig", "grapefruit", "grapes", "kiwi", "lime", "lemon", "mango", "melon", "nectarine", "orange", "pear", "pineapple", "peach", "pomegranate", "quince", "tangerine", "watermelon")
    first_letter = input("Input the first letter of fruit name: ")
    counter = 0
    for fruits in range(len(fruit_basket)):
        if (fruit_basket[fruits][0]) == first_letter:
            counter += 1
            print(fruit_basket[fruits])
    print(f"There are {counter} fruits in our fruits basket, whose name starts with a letter '{first_letter}'")
#Fruits()

#Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
print("Сессия диалога начата. Для окончания напишите 'пока'")

bot =  {"привет": "Здравствуй!",
            "как тебя зовут?": "Виктория",
            "как дела?": "Отлично!",
            "как настроение?": "Замечательное!",
            "что делаешь?": "Думаю о тайнах бытия",
            "пока": "До свидания!"
}

question = input().lower()
while question != "пока":
    if question in bot:
        print(bot.get(question))
    else:
        print("Я затрудняюсь ответить")
    question = input().lower()




        




