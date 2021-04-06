
def row(row_max, prodA, prodB, target):
    return [['  ', '**', '++', '__'][(a >= row_max) +\
        (row_max <= a+b) + 3*(t +10 == row_max)] \
        for a, b, t in zip(prodA, prodB, target)]
​
def rows(pA, pB, target):
    for rmax in range(max(target)+10, 0, -10):
        yield ' '.join([str(rmax), '|'] + row(rmax, pA, pB, target) + ['|'])
    yield '   | Mo Tu We Th Fr Sa Su |'
​
def column_chart(prodA, prodB, target):
    return '\n'.join(rows(prodA, prodB, target))

