
def peel_layer_off(lst):
    if len(lst) <= 2:
        return []
    else:
        newlst = []
        middle_layer = lst[1:-1]
        for x in range(len(middle_layer)):
            middle_layer[x].pop()
            a = middle_layer
        for x in range(len(a)):
            newlst.append(a[x][1:])
    return newlst

