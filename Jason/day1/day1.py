target = 2020
nums = []
with open('input.txt') as my_file:
    for num in my_file:
        nums.append(int(num))

for num in nums:
    if nums.__contains__(target - num):
        print(num * (target - num))

# 3sum (but really bad. there's a better way with pointers on a sorted array that executes 2 sum with a third value
# but i'm too lazy for it rn so gonna leave it as a exercise to you joe
two_sums = []
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i != j and i != k and j != k and (nums[i] + nums[j] + nums[k] == target):
                print(nums[i] * nums[j] * nums[k])

# 987339
# 259521570