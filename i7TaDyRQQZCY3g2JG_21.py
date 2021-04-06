
def lcm(nums):
    if len(nums) ==1:
        return nums[0]
    nums.sort()
    maxnum = nums[-1]
    secondmaxnum = nums[-2] 
    product = 1
    for i in nums:
        product *= i
        
    if maxnum - secondmaxnum ==1:
        return int(product/2)
​
    for i in range(maxnum, product+1, maxnum):
        divisible = True
        for j in nums:
            if i % j != 0:
                divisible = False
​
        if divisible:
            return i

