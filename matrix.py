matrix = [
[2, 4, 6, 8],
[8, 6, 4, 2],
[1, 2, 3, 4],
]
print(matrix)
print('\n')

mat = [[x +10 for x in y] for y in matrix]
print(mat)
print('\n')

mat2 = [[x * 10 for x in y] for y in matrix]
print(mat2)


