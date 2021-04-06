
def can_build(s1, s2):
    result = True
    for i in s2:
        if i not in s2:
            result = False
        if s1.count(i) < s2.count(i):
            result = False
    if result is False:
        return False
    else:
        return True

