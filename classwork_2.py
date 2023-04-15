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
    substring = input("Введите подстроку: ")
    phrase = input("Введите фразу: ")
    lenght_substring = len(substring)
    lenght_phrase = len(phrase)
    counter = 0

    for i in range(lenght_phrase):
        if phrase[i: i + lenght_substring] == substring:
            counter = counter + 1
    print(f"Подстрока {substring} встречатеся {counter} раз(-а) во фразе {phrase}")

#TASK_3()


# Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...

def TASK_4():
    number = int(input("Input a number: "))
    element = 1
    numbers = []
    for i in range(number):
        numbers.append(element)
        element *= -3
    print(numbers) 

#TASK_4()