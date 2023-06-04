import numpy as np
#1 Вариант решения
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
new_matrix = [new[::-1] for new in matrix[::-1]]
print(new_matrix)
#2 Вариант решения
result = []
for i in matrix[::-1]:
    for j in i[::-1]:
        result.append(j)
result = np.array(result).reshape(4, 4)
print(result)
