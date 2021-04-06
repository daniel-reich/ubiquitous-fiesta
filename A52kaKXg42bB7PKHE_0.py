
def num_then_char(lst):
    nums, chars = [], []
    for i in sum(lst, []):
        chars.append(i) if type(i) == str else nums.append(i)
    vals = iter(sorted(nums) + sorted(chars))
    return [[next(vals) for _ in range(len(i))] for i in lst]

