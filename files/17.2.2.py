name_file = input().strip()
real_file = open(name_file, 'r')

list_1 = list(real_file)
print(list_1[-2])

real_file.close()