
def duplicate_nums(nums):
    a = [i for i in set(nums) if nums.count(i) > 1] 
    return None if a==[] else sorted(a)

