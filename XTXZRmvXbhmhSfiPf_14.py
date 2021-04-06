
nums = [-1, 2, -4, 20, -1, 2, -4, -4, 2, -1]
def single_number(nums):
    sing = [x for x in set(nums) if nums.count(x)==1]
    return sing[0]
single_number(nums)

