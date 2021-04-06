
def antipodes_average(lst):
    L = len(lst)
    if L % 2 == 0:
        left, right = lst[:L//2], lst[L//2:][::-1]
    else:
        left, right = lst[:L//2], lst[L//2+1:][::-1]
    return [(left[i] + right[i]) / 2 for i in range(L//2)]

