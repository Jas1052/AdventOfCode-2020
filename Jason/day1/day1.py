target = 2020
nums = []
with open('input.txt') as my_file:
    for num in my_file:
        nums.append(int(num))

inverse = []
for num in nums:
    inverse.append(target - num)

for num in nums:
    if inverse.__contains__(num):
        print(num * (target - num))

# 987339
