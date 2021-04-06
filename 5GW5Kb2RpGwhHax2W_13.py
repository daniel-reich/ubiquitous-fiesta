
def spiral_transposition(lst):
    n,idx = [],[]
    while len(lst) > 1:
        top = lst[0]
        bottom = lst[-1]
        left,right = [],[]
        for sub in lst[1:-1]:
            left.append(sub[0])
            right.append(sub[-1])
        spiral = top + right + bottom[::-1] + left[::-1]
        n += spiral
        del lst[0]
        del lst[-1]
        for sub in lst:
            del sub[-1]
            del sub[0]
    if lst:
        n += lst[0]
    return n

