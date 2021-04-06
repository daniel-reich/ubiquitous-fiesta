
def alternate_sort(lst):
    nums, chars, res = [], [], []
    for i in lst:
        nums.append(i) if type(i) == int else chars.append(i) 
    for i in zip(sorted(nums), sorted(chars)):
        res += i
    return res

