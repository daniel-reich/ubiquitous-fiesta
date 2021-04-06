
def min_difference_pair(nums):
    nums.sort()
    return list(min([i for i in zip(nums, nums[1:])], key=lambda x: x[1] - x[0]))

