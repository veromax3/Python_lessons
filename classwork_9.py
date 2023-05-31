import numpy as np

nums_1 = [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
nums_2 = [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
nums_3 = [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]

matrix = [nums_1, nums_2, nums_3]
result = np.corrcoef(matrix)
# print(result)


size = 10
numbers = np.random.randint(5, 15, size)
print(numbers)
print(sum(numbers)/len(numbers))

