
def simple_comp(ls1, ls2):
    if ls1 is None or ls2 is None:
        return False
    ls1.sort(key=abs)
    ls2.sort(key=abs)
    return (all(a * a == b for a, b in zip(ls1, ls2))
            if len(ls1) == len(ls2) else False)

