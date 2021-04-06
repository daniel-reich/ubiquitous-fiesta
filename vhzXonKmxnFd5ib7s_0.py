
def matrix_multiply(a, b):
    if len(b) != len(a[0]):
        return 'invalid'
​
    matrix = []
    for row in a:
        group = []
        for col in zip(*b):
            group.append(sum(r*c for r, c in zip(row, col)))
        matrix += [group]
    return matrix

