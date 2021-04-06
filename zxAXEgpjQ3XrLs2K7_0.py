
def merge_sort(lst1, lst2):
    return sorted(lst1 + lst2, reverse=lst1[1] < lst1[0])

