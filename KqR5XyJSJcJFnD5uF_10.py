
def median(nums):
    l = len(nums)//2
    if len(nums) % 2 == 0:
        return round(sum(nums[l-1:l+1])/2,1)
    return nums[l]

