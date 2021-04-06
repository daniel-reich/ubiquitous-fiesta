
def is_repeated(s):
    for i in (1, 2, 3, 4, 6, 8, 12):
        if s.replace(s[:i], '') == '':
            return 24/i
    return False

