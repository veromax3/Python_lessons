# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию

import random
def Random_bigger_5():
    list_length_1 = int(input("Input list length: "))
    numbers_1 = [random.randint(1, 10) for i in range(list_length_1)]
    bigger_5 = list(filter(lambda x: x > 5, numbers_1))
    print(f"The number(s) in list {numbers_1}, that bigger than 5, is(are): {bigger_5}")
#Random_bigger_5()

# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.

def  Increasing_sequence():
    list_length_2 = int(input("Input list length: "))
    numbers_2 = [random.randint(1, 100) for i in range(list_length_2)]
    print(f"Random list is: {numbers_2}")
    seq = []
    copy_i = -1
    i = random.randint(0, list_length_2 -1)
    while i < list_length_2 - 1:
        if i > copy_i:
            seq.append(numbers_2[i])
            copy_i = i
            i = random.randint(1, list_length_2)
        else:
            i = random.randint(1, list_length_2)
    print(f"Random sequence from list: {seq}")

    i = 0
    counter = 0
    while counter < len(seq) - 1:
        if seq[i] > seq[i + 1]:
            seq.pop(i + 1)
        else:
            counter += 1
            i += 1  
    print(f"The increasing random sequence from random list is: {seq}")

#Increasing_sequence()

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.

def Repeats():
    list_length_3 = int(input("Input list length: "))
    numbers_3 = [random.randint(1, 10) for i in range(list_length_3)]
    print(numbers_3)
    repeats = 0
    i = 0
    while i < len(numbers_3):
        counter = numbers_3.count(numbers_3[i])
        if counter > 1:
            print(f"{numbers_3[i]} repeats in list {counter} times")
            repeats += 1
            numbers_3.remove(numbers_3[i])
        i += 1
    
    print(f"There are {repeats} repeats in list")
    print(f"Unique sequence is {numbers_3}")

# Repeats()