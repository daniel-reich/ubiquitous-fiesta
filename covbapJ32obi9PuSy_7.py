
def diamond_arrays(x):
    lst = []
    for a in range(1,x+1):
        lst.append(a * list(str(a)))
        for z in lst:
            for i,y in enumerate(z):
                z[i] = int(y)
    return lst[:-1] + lst[::-1]

