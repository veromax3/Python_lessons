import numpy as np

# Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.
def Unique_el():
    print("Task 1")
    size = 10
    numbers = np.random.randint(1, 10, size)
    print(f"The array is {numbers}")
    unique_numbers, counts_unique_num = np.unique(numbers, return_counts = True)
    print(f"Unique elements {unique_numbers}")
    print(f"Numbers of unique elements {counts_unique_num}")
    print()
Unique_el()

# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

def Matrix1():
    print("Task 2")
    size = 5, 5
    matrix_2D = np.random.randint(0, 2, size)
    print("The 2D array is") 
    print(matrix_2D)
    matrix_coef = np.corrcoef(matrix_2D)
    print("Correlation coefficients between strings are")
    print(matrix_coef)
    count = 0
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if matrix_coef[i][j] == 1:
                count += 1
    if count > size[0]:
        print("The array contains the same strings")
    else:
        print("The strings are unique")
    print()

Matrix1()


# Задача 3. Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

def Matrix2():
    print("Task 3")
    size = np.random.randint(2, 8), np.random.randint(2, 8)
    print(f"The random size of array is {size}")
    matrix_2D_rand = np.random.randint(1, 10, size)
    print(matrix_2D_rand)
    index_max = np.argmax(matrix_2D_rand)
    index_min = np.argmin(matrix_2D_rand)
    print(f"The maximum index is [{index_max}], the minimum index is [{index_min}]")
    main_diagonal = np.diag(matrix_2D_rand)
    print(f"The main diagonal of array is {main_diagonal}")

Matrix2()



