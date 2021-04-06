
def tree(h):
    return [' '*(h - i - 1) + '#'*(2*i + 1) + ' '*(h - i - 1) for i in range(h)]

