
def smallest(bound):
    nums = [i for i in range(1, bound+1)]
    prod = 1
    for i in range(0, len(nums)-1):
        prod *= int(nums[i])
        for j in range(i+1, len(nums)):
        
            if nums[j] % nums[i] == 0 and nums[j] >= nums[i]:
                nums[j] = nums[j]/nums[i]
    else:
        prod *= int(nums[-1])
    return prod

