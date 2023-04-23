# Задача 0. Дан список, заполненный случайными числами от 0 до 10. Определите, является ли сумма всех элементов чётной.

import random
# length = 7
# # numbers = [0] * length
# # for index in range(length):
# # #     numbers[index] = random.randint(0, 100)
# # print(numbers)

# numbers = [random.randint(0, 10) for i in range(length)]
# print(numbers)
# sum = 0
# for index in range(length):
#     sum += numbers[index]
# print(sum)
# if sum % 2 == 0:
#     print("Сумма четная")
# else:
#     print("Сумма нечетная")


# Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня. Определите в какой период выпало больше осадков: в первой или второй половине июня.

def Precipitation():
    length_month = 30
    precipitation = []
    precipitation = [random.randint(0, 25) for index in range(length_month)]
    print(precipitation)
    first_half_month = 0
    second_half_month = 0
    for day in range(length_month // 2):
        first_half_month += precipitation[day]
    for day in range(length_month // 2, length_month):
        second_half_month += precipitation[day]
    if first_half_month > second_half_month:
        print(f"There was more precipitation  in the first half of the month ({first_half_month}) than in the second ({second_half_month})")
    else:
        print(f"There was more precipitation in the second half of the month ({second_half_month}) than in the first ({first_half_month})")

#Precipitation()

# Задача 2. Напишите программу, которая позволит пользователю заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета

def questionnaire():
    dictionary = dict (Name = input("Input your name: "),
                    Age = input("Input your age: "),
                    Hobbie = input("Input your hobbie: "),
                    Favorite_animal = input("Input your favorite animal: "))
    for (keys, value) in dictionary.items():
        print(keys + ": " + value)

#questionnaire()

# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел.
def Password():
    symbols = "ABCDEFGHIKLMNOPQRSTVXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password_length = int(input("Input the password length: "))
    password = [symbols[random.randint(0, len(symbols))] for el in range(password_length)]
    print(password)

Password()

# Задача 4. Ручка стоит – 5 рублей, карандаш – 3 рубля, ластик – 4 рубля.
# Кассир последовательно вводит в программу позиции из чека «ручка», «карандаш», «ластик».
# Ввод заканчивается, когда введено слово «стоп». Определите сумму чека.