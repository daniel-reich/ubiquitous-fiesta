
lcm_three = lambda nums: lcm([lcm([nums[0],nums[1]]), nums[2]])
def lcm(nums):
    mx = max(nums)
    while mx%nums[0] or mx%nums[1]:
        mx += 1
    return mx

