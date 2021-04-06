
def count_boomerangs(lst):
    return len([1 for i in range(1, len(lst)-1)
                if (lst[i-1] == lst[i+1]) and (lst[i-1] != lst[i])])

