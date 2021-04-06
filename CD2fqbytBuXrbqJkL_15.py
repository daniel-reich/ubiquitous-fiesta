
def can_build(p1,p2):
    p1 = ''.join(p1.split())
    p2 = ''.join(p2.split())
    l = []
    for a in p1:
        if p1.count(a) > p2.count(a):
            return False
    return True

