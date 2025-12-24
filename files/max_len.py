with open('lines.txt', 'r') as file :
    lines = file.readlines()
max_len = max( len(line.rstrip('\n')) for line in lines)
for line in lines :
    if len(line.rstrip('\n')) == max_len :
        print(line, end ='')
