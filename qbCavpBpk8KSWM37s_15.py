
def largest_gap(lst):
    lst = sorted(set(lst))
    return max( (lst[i] - lst[i-1] for i in range(1,len(lst))))

