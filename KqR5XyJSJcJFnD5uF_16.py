
def median(nums):
    middle = nums[len(nums) // 2]
    if len(nums) % 2 == 0:
        middle = (nums[(len(nums) // 2) - 1] + middle) / 2
    return middle

