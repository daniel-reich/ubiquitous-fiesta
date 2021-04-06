
def is_long_pressed(original, typed):
    last, p = original[0], 1
    if last != typed[0]: return False
    for i in typed[1:-1]:
        if i == original[p]:
            last = i; p += 1; continue
        elif i == last: continue
        else: return False
    return original[-1] == typed[-1]

