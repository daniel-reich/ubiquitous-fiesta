
def widen_streets(lst, n):
    lst = [list(x) for x in list(zip(*lst[::-1]))]
​
    a = []
    for x in lst :
        if x[0] == ' ':
            for i in range(n):
                a.append(x)
        else:
            a.append(x)
    return [''.join(x) for x in list(zip(*a))][::-1]

