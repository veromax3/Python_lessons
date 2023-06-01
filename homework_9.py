import numpy as np

# Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

def unique_el():
    size = 10
    numbers = np.random.randint(1, 10, size)
    print(numbers)
    
    unique_numbers, counts_unique_num = np.unique(numbers, return_counts = True)
    print(f"Unique elements: {unique_numbers}")
    print(f"Numbers of unique elements: {counts_unique_num}")
#  unique_el()

# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

def Matrix():
    size = 5, 5
    matrix_2D = np.random.randint(0, 2, size)
    print(matrix_2D)
    matrix = np.corrcoef(matrix_2D)
    print(matrix)
    count = 0
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if matrix[i][j] == 1:
                count += 1
                print(count, i, j)
    if count > size[0]:
        print("The array contains the same strings")
    else:
        print("The array does not contains the same strings")
Matrix()

# Задача 3. Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.


# def matrix2():
#     size = np.random.randint(2, 10), np.random.randint(2, 10)
#     print(size)
#     matrix_2D = np.random.randint(1, 10, size)
#     print(matrix_2D)
#     index_max = np.argmax(matrix_2D)
#     print(index_max)

# matrix2()



