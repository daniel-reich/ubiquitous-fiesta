
def max_product(nums):
    nums = sorted(nums)
​
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
​
def min_product(nums):
    nums = sorted(nums)
    
    return min(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])

