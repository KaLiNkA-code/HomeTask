import numpy as np


"""111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"""

matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

"""222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"""

matrix = np.ones((3, 3))
matrix = np.pad(matrix, pad_width=1)
print(matrix)

"""333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"""

Array1 = [0, 10, 20, 40, 60, 80]
Array2 = [10, 30, 40, 50, 70]

a = np.union1d(Array1, Array2)
print(a)

"""444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444"""


len1 = int(input(''))
len2 = int(input(''))


p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result = np.outer(p, q)
