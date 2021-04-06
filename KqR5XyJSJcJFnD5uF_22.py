
def median(nums):
    import math
    if len(nums)%2 != 0:
        index = math.floor(len(nums) / 2)
        return nums[index]
​
    else: 
        index = math.floor(len(nums) / 2)
        index_1 = index - 1
        return round((nums[index] + nums[index_1]) / 2,1)

