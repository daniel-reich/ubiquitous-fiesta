
def check_pattern(s):
    n = len(s)
    for k in range(2, len(s) // 2 + 1):
        pattern = s[:k]
        long = pattern * (2 + n // k)
        if long[:n] == s and n >= 2 * k:
            return True
    return False
​
def complete_pattern(s):
    unique = set(s.replace('_', ''))
    if len(s) == 2:
        return list(unique)[0]
    for c in unique:
        s2 = s.replace('_', c)
        if check_pattern(s2):
            return c

