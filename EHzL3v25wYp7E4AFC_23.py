
def can_build(s1, s2):
    l = list(s1)
    for item in s2:
        if item not in s1:
            return False
        if s2.count(item) > s1.count(item):
            return False
    return True

