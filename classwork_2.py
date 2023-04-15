# Дано число N. Найти всего его делители. Для каждого указать четный он или нечетный.



def check_even(i):
    if i % 2 == 0:
        return "четное"
    else:
        return "нечетное"
        
def TASK_1():
    number = int(input("Введите число: "))
    for i in range(1, number + 1):
        if number % i == 0:
            print(f"{i} - {check_even(i)} ")

#TASK_1()

# Выведите таблицу истинности для выражения ¬X ∨ Z.

def TASK_2():
    for i in range (0, 2):
        for j in range (0, 2):
            print(f"{i}| {j} | {int(not i or j)}")

#TASK_2()

# Задача 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.

def TASK_3():
    substringn = input("Введите подстроку: ")
    phrase = input("Введите фразу: ")
    