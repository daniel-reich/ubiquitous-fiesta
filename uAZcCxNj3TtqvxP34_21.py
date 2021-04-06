
def mode(nums):
    maxCount = 0
    for num in nums:
        if nums.count(num) > maxCount:
            maxCount = nums.count(num)
    return sorted(set([i for i in nums if nums.count(i) == maxCount]))

