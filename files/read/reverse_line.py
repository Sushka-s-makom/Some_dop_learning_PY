with open('text.txt', 'r') as file:
    line = file.readline()
    print(line[::-1])
