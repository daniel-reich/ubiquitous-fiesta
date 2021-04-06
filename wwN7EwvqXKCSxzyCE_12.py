
def reorder_digits(lst, direction):
    return [f(x, direction) for x in lst]
​
def f(x, d):
    s = ''.join(sorted(str(x)))
    if d == 'desc':
        s = s[::-1]
    return int(s)

