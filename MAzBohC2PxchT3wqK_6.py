
def shadow_sentence(a, b):
    lst_a, lst_b = a.split(), b.split()
    if len(lst_a) == len(lst_b):
        for x, y in zip(lst_a, lst_b):
            if len(x) != len(y) or set(x) & set(y):
                return False
        return True
    return False

