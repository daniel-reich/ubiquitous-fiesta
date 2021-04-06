
message = ''
def bingo_check(b):
    if (set(b[i][i] for i in range(5)) == {'x'} or
            set(b[i][4 - i] for i in range(5)) == {'x'}):
        return True
    for i in range(5):
        if set(b[i]) == {'x'} or set(b[r][i] for r in range(5)) == {'x'}:
            return True
    return False

