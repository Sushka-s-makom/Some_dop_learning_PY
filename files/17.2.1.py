
name_file = input().strip()
real_file = open(name_file, 'r')

print(real_file.read(), end='')

real_file.close()