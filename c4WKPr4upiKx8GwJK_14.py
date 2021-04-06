
def duplicate_nums(nums):
    lst=[]
    for i in set(nums):
        if nums.count(i)>1:
            lst.append(i)
    if len(lst)==0:
        return None
    else:
        return sorted(lst)

