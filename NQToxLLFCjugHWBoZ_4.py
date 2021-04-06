
def sort_by_character(lst, n):
    lst1 = sorted([(j[n-1],i) for i,j in enumerate(lst)])
    return [lst[lst1[i][1]] for i in range(len(lst1))]

