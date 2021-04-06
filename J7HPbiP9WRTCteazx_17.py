
def n_differences(lst):
    while len(lst) > 1:
        lst = [(lst[i+1] - lst[i]) for i in range(len(lst)-1)]
    return lst[0]

