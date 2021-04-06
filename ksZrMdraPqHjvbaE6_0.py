
def largest_even(lst):
    res = -1
    for x in lst:
        if not x % 2 and x > res:
            res = x
    return res

