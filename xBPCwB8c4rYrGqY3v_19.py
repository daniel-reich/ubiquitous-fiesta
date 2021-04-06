
def missing(lst):
    common_diff = min(lst[1]-lst[0],lst[2]-lst[1])
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i]!=common_diff:
            return lst[i]+common_diff

