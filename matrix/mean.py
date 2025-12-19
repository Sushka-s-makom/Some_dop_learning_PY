n = int(input())

for i in range(n):
    row = list(map(int, input().split()))
    mean = sum(row)/n
    count = 0
    for a in row:
        if a > mean:
            count += 1
    print(count)
