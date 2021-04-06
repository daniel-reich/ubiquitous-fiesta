
def almost_uniform(nums):
    max_length = 0
    for i in range(len(nums)):
       if nums[i] - 1 in nums:
            cnt = nums.count(nums[i]) + nums.count(nums[i]-1)
            max_length = max(max_length, cnt)
       if nums[i] + 1 in nums:
            cnt = nums.count(nums[i]) + nums.count(nums[i]+1)
            max_length = max(max_length, cnt)
    return max_length

