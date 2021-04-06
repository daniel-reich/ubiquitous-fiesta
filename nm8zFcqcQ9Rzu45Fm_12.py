
def bridge_shuffle(lst1, lst2):
    res = []
    for _ in range(max(len(lst1), len(lst2))):
        if lst1: res.append(lst1.pop(0))
        if lst2: res.append(lst2.pop(0))
    return res

