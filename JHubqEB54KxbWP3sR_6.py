
def dist(line, x, y):
    left, right = line.split('=')
    idx = right.index('x')
    a = eval(right[:idx])
    c = eval(right[idx + 1:])
    numerator = abs(eval('{} * ({}) - ({}) + ({})'.format(a, x, y, c)))
    return round(numerator / pow(a * a + 1, 0.5), 2)

