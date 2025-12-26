real_file = open('prices.txt', 'r')

total = 0

for line in real_file:
    name, count, prices = line.split('\t')
    total += int(count) * int(prices)
print(total)


