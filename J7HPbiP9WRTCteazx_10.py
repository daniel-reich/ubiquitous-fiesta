
def n_differences(lst):
    lst = [lst[n+1]-lst[n] for n in range(len(lst)-1)]
    return (lst[0] if len(lst)==1 else n_differences(lst))

