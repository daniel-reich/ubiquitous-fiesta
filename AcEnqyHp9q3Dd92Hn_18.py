
def multiply_nums(nums):
    new = nums.split(", ")
    lst = [int(n) for n in new]
    c = 1
    for n in lst:
        c *= n
    return c

