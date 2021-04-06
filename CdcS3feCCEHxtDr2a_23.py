
def clear_ordering(lst):
    while len(lst) > 1:
        removed = False
        for p in lst[1:]:
            if lst[0][0] == p[1]:
                lst[0][0] = p[0]
                lst.remove(p)
                removed = True
            elif lst[0][1] == p[0]:
                lst[0][1] = p[1]
                lst.remove(p)
                removed = True
        if not removed:
            return False
    return True

