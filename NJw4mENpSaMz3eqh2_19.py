
def is_undulating(n):
    n = str(n)
    if len(n) < 3 or len(set(n)) != 2:
        return False
    last = n[0]
    for cur in n[1:]:
        if last == cur:
            return False
        last = cur
    return True

