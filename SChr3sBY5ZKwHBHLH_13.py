
def sort_it(lst):
    x = [i if type(i) == int else i[0] for i in lst]
    y = sorted(x)
    a = []
    for i in y:
        if i in lst:
            a.append(i)
        else:
            a.append([i])
    return a

