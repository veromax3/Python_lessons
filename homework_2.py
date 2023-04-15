# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.

def TASK_1():
    temp_num = 1
    factorial = 1
    number = int(input("Input a number: "))
    for i in range (1, number + 1):
        while temp_num <= i:
            factorial = factorial * temp_num
            temp_num = temp_num + 1
        print(factorial, end = " ")

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z

def TASK_2():
    print("X| Y | Z | ¬(X ∧ Y) ∨ Z")
    for i in range (0, 2):
        for j in range (0, 2):
            for k in range (0, 2):
                print(f"{i}| {j} | {k} | {(int(not (i and j) or k))}")


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй

def TASK_3():
    substring = input("Input a substring: ")
    phrase = input("Input a phrase: ")
    lenght_substring = len(substring)
    lenght_phrase = len(phrase)
    

    for i in range(lenght_substring):
        counter = 0
        for j in range (lenght_phrase):
            if substring[i] == phrase[j]:
                counter = counter + 1
        print(f"The symbol {substring[i]} occur {counter} time in {phrase}")
    
#TASK_3() 


