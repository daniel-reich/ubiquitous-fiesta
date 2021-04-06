
def is_authentic_skewer(s):
    vows = 'AOUIE'
    for c in (s[0], s[-1]):
        if c in vows or c == '-':
            return False
    sep_len = 0
    i = 1
    while i < len(s) and s[i] == '-':
        sep_len += 1
        i += 1
    if i == len(s):
        return False
    if sep_len == 0:
        return False
    if s[i] not in vows:
        return False
    last_cons = False
    sep = '-' * sep_len
    i += 1
    while i + sep_len < len(s):
        if s[i:i+sep_len] != sep:
            return False
        if s[i+sep_len] == '-' or (s[i+sep_len] in vows) != last_cons:
            return False
        i += sep_len + 1
        last_cons = not last_cons
    return i == len(s)

