from random import randint

real_file = open('lines.txt', 'r')

list_1 = list(real_file)
n = len(list_1)
print(list_1[randint(0, n)])

real_file.close()