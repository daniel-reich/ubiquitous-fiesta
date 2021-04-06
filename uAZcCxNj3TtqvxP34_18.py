
def mode(nums):
    mode_count = max(nums.count(i) for i in nums)
    return sorted(i for i in set(nums) if nums.count(i) == mode_count)

