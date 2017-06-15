# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
matrix = [
    [2, 25, 8.9],
    [4, 19, 6],
    [4, 8, 0],
    [10, 11, 136],
]
a = []
b = []
c = []
for row in matrix:
    print(row)
for col in matrix:
    a.append(col[0])
    b.append(col[1])
    c.append(col[2])
    pass
print('1st collumn:', a)
print('2nd collumn:', b)
print('3rd collumn:', c)