
def greater_than_sum(nums):
    return all([nums[i] > sum(nums[0:i]) for i in range(1, len(nums))])

