
def sum_neg(nums):
    if not nums: return []
    return [len([n for n in nums if n > 0]), sum(n for n in nums if n < 0)]

