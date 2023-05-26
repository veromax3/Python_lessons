import random
import time

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

