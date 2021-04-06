
def is_ascending(s, last=0, l=0):
    if len(s) == 0:
        return True
    if last == 0:
        L = len(s)
        for l in range(1, L // 2 + 1):
            if L % l == 0:
                last = int(s[:l])
                if is_ascending(s[l:], last, l):
                    return True
        return False
    if len(s) < l:
        return False
    if len(s) == l:
        return int(s) == last + 1
    cur = int(s[:l])
    if cur != last + 1:
        return False
    return is_ascending(s[l:], cur, l)

