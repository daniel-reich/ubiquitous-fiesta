
def sum_of_slices(lst):
    ans = []
    S = 0
    for k in lst:
        if S + k > 100:
            ans.append(S)
            S = k
        else:
            S += k
    ans.append(S)
    return ans

