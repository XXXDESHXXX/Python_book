nums = [1, 2, 3, 1, 2, 3]
nums.sort()
k = 3
n = len(nums) - 1
i = 0
j = 1
while i <= n:
    if nums[i] == nums[j] and abs(i - j) <= k:
        print(True)
    else:
        i += 1
        j += 1
print(False)