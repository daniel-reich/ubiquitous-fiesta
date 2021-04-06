
def clear_ordering(lst):
    a=set(lst[i][0] for i in range(len(lst)))
    b=set(lst[i][1] for i in range(len(lst)))
    if len(a)<len(lst) or len(b)<len(lst):
        return False
    return True

