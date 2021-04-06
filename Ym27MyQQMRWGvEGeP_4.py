
def is_consecutive(s, last=0, l=0, direction="asc"):
    if len(s) == 0:
        return True
    if last == 0:
        L = len(s)
        for l in range(1, L // 2 + 1):
            if L % l == 0:
                last = int(s[:l])
                if is_consecutive(s[l:], last, l, "asc") or is_consecutive(s[l:], last, l, "desc"):
                    return True
        return False
    if len(s) < l:
        return False
    if len(s) == l:
        return (direction == "asc" and int(s) == last + 1) or (direction == "desc" and int(s) == last - 1)
    cur = int(s[:l])
    if (direction == "asc" and cur != last + 1) or (direction == "desc" and cur != last - 1):
        return False
    return is_consecutive(s[l:], cur, l, direction)

