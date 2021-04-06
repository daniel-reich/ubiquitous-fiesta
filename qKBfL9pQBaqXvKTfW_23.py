
def sum_of_slices(lst):
    ans = []
    tot = 0
    for x in lst:
        tot += x
        if tot > 100:
            ans.append(tot - x)
            tot = x
    if tot:
        ans.append(tot)
    return ans

