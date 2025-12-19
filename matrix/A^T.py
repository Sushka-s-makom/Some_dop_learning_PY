n, m = int( input()), int(input())
matrix =[]

for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input())
    matrix.append(row)


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

print()

# вывод транспонированной матрицы
for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()
