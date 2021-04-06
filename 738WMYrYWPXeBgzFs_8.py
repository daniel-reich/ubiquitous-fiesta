
def is_valid(txt):
    c = [txt.count(i) for i in set(txt)]
    s = list(set(c))
    if len(s) > 2: return "NO"
    if len(s) == 1: return "YES"
    if (len(s) == 2 and abs(s[0]-s[1]) == 1):
        if (c.count(s[0]) ==1 or c.count(s[1]) == 1):
            return "YES"
    return "NO"

