
import collections
def is_autobiographical(n):
    s = str(n)
    if len(s) > 10:
        return False
    cnts = collections.Counter(s)
    for i, x in enumerate(s): 
        if x == '0':
            if str(i) in cnts:
                return False
        else:
            if cnts.get(str(i), -1) != int(x):
                return False
    return True

