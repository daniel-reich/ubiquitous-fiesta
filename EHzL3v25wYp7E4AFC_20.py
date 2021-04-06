
def can_build(s1, s2):
    l1 = [l for l in s1]
    try:
        l2 = [l1.remove(l) for l in s2]
    except ValueError:
        return False
    return True

