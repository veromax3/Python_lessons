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
    print(numbers_2)
    for i in range(list_length_2):
        if numbers_2[i] > 

Increasing_sequence()




# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.