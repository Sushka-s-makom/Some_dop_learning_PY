with open('class_scores.txt', 'r') as fin, open('new_scores.txt', 'w') as fout:
    for line in fin:
        parts = line.split()
        parts[1] = str(min(int(parts[1]) + 5, 100))
        print(*parts, file=fout)
