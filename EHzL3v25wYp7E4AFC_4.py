
def can_build(s1, s2):
    s1 = [x for x in s1]
    for i in range(len(s2)):
        if s2[i] in s1:
            s1.remove(s2[i])
        else:
            return False
    return True

