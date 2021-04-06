
def duplicate_nums(nums):
    ls=list(set([i for i in nums if nums.count(i)>1]))
    if len(ls)>0:
        return sorted(ls)
    return None

