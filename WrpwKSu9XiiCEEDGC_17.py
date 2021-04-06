
def can_alternate(s):
    return True if s.count('0') - s.count('1') in [-1,1,0] else False

