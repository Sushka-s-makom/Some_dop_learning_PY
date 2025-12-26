with open('data.txt', 'r') as file :
    lines = list(file.readlines())
    for line in (lines[::-1]) :
        print(line, end='')