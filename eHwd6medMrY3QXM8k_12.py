
def ascending(txt):
    L = len(txt)
    for l in range(1, L // 2 + 1):
        valid = True
        if L % l != 0:
            continue
        last = int(txt[:l])
        for k in range(1, L // l):
            cur = int(txt[l*k:l*k+l])
            if cur != last + 1:
                valid = False
                break
            last = cur
        if valid:
            return True
    return False        
​
def descending(txt):
    L = len(txt)
    for l in range(1, L // 2 + 1):
        valid = True
        if L % l != 0:
            continue
        last = int(txt[:l])
        for k in range(1, L // l):
            cur = int(txt[l*k:l*k+l])
            if cur != last - 1:
                valid = False
                break
            last = cur
        if valid:
            return True
    return False        
​
def is_consecutive(s):
    return ascending(s) or descending(s)

