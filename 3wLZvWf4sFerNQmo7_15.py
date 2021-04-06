
def neutralise(s1, s2):
    n = ''
    for i, j in zip(s1, s2):
        if i == '+' and j == '+':
            n += '+'
        if i == '-' and j == '-':
            n += '-'
        if i != j:
            n += '0'
    return n

