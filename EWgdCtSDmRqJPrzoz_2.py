
def peel_layer_off(lst):
    l = []
    for sub in lst[1:-1]:
        l.append(sub[1:-1])
    return l

