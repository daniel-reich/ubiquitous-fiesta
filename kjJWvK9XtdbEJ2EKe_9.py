
def sort_array(lst):
    for iter_num in range(len(lst) - 1, 0, -1):
        for x in range(iter_num):
            if lst[x] > lst[x+1]:
                lst[x], lst[x+1] = lst[x+1], lst[x]
    return lst

