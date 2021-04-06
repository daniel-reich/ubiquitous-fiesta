
def replace_next_largest(lst):
    res = []
    for x in lst:
        if x == max(lst):
            res.append(-1)
        else:
            nums = sorted(n for n in lst if n > x)[::-1] + [x]
            idx = nums.index(x)
            res.append(nums[idx - 1])
    return res

