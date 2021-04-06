
def min_difference_pair(nums):
    nums.sort()
    arr = []
    for i in range(len(nums))[:-1]:
        arr.append(abs(nums[i] - nums[i + 1]))
​
    return nums[arr.index(min(arr)):arr.index(min(arr))+2]

