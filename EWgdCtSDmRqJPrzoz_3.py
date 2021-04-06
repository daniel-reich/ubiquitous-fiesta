
def peel_layer_off(lst):
    lst1 = []
    for i in lst[1:-1]:
        lst1.append(i[1:-1])
    return lst1

