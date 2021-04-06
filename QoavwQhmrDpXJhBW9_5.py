
def flip_list(lst):
    b = []
    if lst == []:
        return b
    a = 0
    for i in lst:
        if type(i) == list:
            b.append(i[0])
        else:
            b.append(list())
            b[a].append(i)
            a += 1
    return b

