with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    i = 1
    for line in fin:
        fout.write(f"{i}) {line}")
        i += 1

