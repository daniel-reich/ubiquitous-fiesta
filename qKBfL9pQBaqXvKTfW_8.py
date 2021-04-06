
def sum_of_slices(lst):
    a = 0
    l = []
    for i in lst:
        if a+i<=100:
            a += i
        else:
            l.append(a)
            a = i
    l.append(lst[-1])
    return l

