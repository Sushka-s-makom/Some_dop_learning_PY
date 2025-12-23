real_file = open('nums.txt', 'r')

nums = real_file.read().split()
a = int(nums[0])
b = int(nums[1])

print(a + b)

real_file.close()