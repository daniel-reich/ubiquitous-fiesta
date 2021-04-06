
def numbers_to_ranges(lst):
    low = [num for num in lst if num - 1 not in lst]
    up = [num for num in lst if num + 1 not in lst]
    return [str(low[i]) if low[i] == up[i] else str(low[i])+ '-' + str(up[i]) for i in range(len(low))]

