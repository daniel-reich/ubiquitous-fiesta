
def merge_sort(lst1, lst2):
    if lst1[0]>lst1[1]:return sorted(lst1 + (lst2))[::-1]
    else:return sorted(lst1 + (lst2))

