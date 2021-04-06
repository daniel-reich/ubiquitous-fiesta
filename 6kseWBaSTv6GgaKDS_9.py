
def next_letters(s):
    if s == "":
        return 'A'
    if s[-1] != 'Z':
        return s[:-1] + chr(ord(s[-1]) + 1)
    s = s[:-1] + 'A'
    for idx in range(len(s) - 2, -1, -1):
        if s[idx] != 'Z':
            return s[:idx] + chr(ord(s[idx]) + 1) + s[idx+1:]
        s = s[:idx] + 'A' + s[idx+1:]
    return 'A' + s

