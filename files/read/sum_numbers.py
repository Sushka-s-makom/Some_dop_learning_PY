with open('numbers.txt', 'r') as file :
    for line in file :
        nums = map(int, line.split())
        print(sum(nums))