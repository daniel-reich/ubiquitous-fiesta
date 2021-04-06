
def advanced_sort(lst):
    sorted_lst = []
    for i in lst :
        if all([sorted_lst[c][0] != i  for c in range(len(sorted_lst))]):
            sorted_lst.append([i]*lst.count(i))
    return sorted_lst

