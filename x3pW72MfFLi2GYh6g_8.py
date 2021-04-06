
def is_scalable(lst):
    val = lst[0]
    for v in lst:
        if abs(v - val) <= 5:
            val = v
        else:
            return False
    return True

