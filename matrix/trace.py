n = int(input())
matrix =[]
tr = 0

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    tr += matrix[i][i]
print(tr)

