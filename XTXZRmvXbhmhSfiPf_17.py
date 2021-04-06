
def single_number(nums):
    s = set(nums)
    for i in s:
        if nums.count(i)==1:return i

