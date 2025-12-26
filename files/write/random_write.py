import random
nums = [random.randint(111, 777) for i in range(25)]
with open('random.txt', 'w') as file1 :
    for i in range(len(nums)) :
        print(nums[i], file = file1)