
def single_number(nums):
    a = set(nums)
    for i in a:
        if nums.count(i) == 1:
            return i

