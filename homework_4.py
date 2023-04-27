#Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

def Prime_factors():
    number_copy = int(input("Input a natural number: "))
    prime_factor = []
    counter = 0
    prime = 2
    number = number_copy
    while number != 1:
        if number % prime == 0:
            number = number // prime
            counter += 1
            prime_factor.append(prime)
        else:
            prime += 1

    print(f"There are {counter} prime factors for natural number {number_copy}: {prime_factor}")

#Prime_factors()

# Задача 2. В первом списке находится информация об ассортименте мороженного, во втором списке - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.

def Ice_cream():
    product_range = {"Соленая карамель", "Шоколадная крошка", "Апельсинка", "Сливочное", "Милка"}
    products_in_stock = {"Соленая карамель", "Сливочное", "Милка"}
    sold_out = set(product_range.difference(products_in_stock))
    print(sold_out)

#Ice_cream()


#Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.

def Pi_Number():
    with open("Pi.txt", "r") as Pi_number:
        number = float(Pi_number.read())
    accuracy = float(input("Input accuracy of number Pi: "))
    counter = 0
    while accuracy != 1:
        accuracy = accuracy * 10
        counter += 1
    Pi = round (number, counter)
    print(f"The rounded number Pi is: {Pi}")
    
#Pi_Number()