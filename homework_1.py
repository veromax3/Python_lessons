# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.

# day_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# day_number = int(input("Input a number of day of the week: "))

# if day_number - 1 >= 0 and day_number - 1 < 7:
#     print(f"Number {day_number} is {day_of_the_week[day_number - 1]}")
# else:
#     print("Error! Input another number")

# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# import math
# Ax = int(input("Input x-coordinate of a point A: ")) 
# Ay = int(input("Input y-coordinate of a point A: ")) 
# Bx = int(input("Input x-coordinate of a point B: ")) 
# By = int(input("Input y-coordinate of a point B: "))

# ABx = Bx - Ax
# ABy = By - Ay
# AB = round(math.sqrt(ABx**2 + ABy**2), 2)
# print(f"Length between A({Ax}, {Ay}) and B({Bx}, {By}) points is {AB}")

# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# x_coordinate = int(input("Input x-coordinate of a point: "))
# y_coordinate = int(input("Input y-coordinate of a point: "))

# if x_coordinate > 0 and y_coordinate > 0:
#     quadNum = 1
# if x_coordinate < 0 and y_coordinate > 0:
#     quadNum = 2
# if x_coordinate < 0 and y_coordinate < 0:
#     quadNum = 3
# if x_coordinate > 0 and y_coordinate < 0:
#     quadNum = 4

# if x_coordinate != 0 and y_coordinate != 0:
#     print(f"The point ({x_coordinate}, {y_coordinate}) lies on {quadNum} quadrant")
# if x_coordinate == 0 and y_coordinate == 0:
#     print(f"The point ({x_coordinate}, {y_coordinate}) lies on axes")
# if x_coordinate == 0 and (y_coordinate > 0 or y_coordinate < 0):
#     print(f"The point ({x_coordinate}, {y_coordinate}) lies on y-axis")
# if y_coordinate == 0 and (x_coordinate > 0 or x_coordinate < 0):
#     print(f"The point ({x_coordinate}, {y_coordinate}) lies on x-axis")

# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

# N_number = int(input("Input a number: "))
# even_step = 2
# count = 2
# print(f"The list from 1 to {N_number} is: ", end ="")
# while count <= N_number:
#     print(count, end = "; ")
#     count += even_step
