
def consecutive_combo(l1, l2):
    c = sorted(l1 + l2)
    if c[-1] - c[0] == len(c) - 1:
        return True
    return False

