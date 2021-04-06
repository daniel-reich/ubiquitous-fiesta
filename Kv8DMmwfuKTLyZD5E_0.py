
def make_dartboard(n):
    row, top = 0, []
    for i in range(n, 0, -2):
        row += int('{:0^{}}'.format('1'*i, n))
        top.append(row)
    bottom = top[::-1][1:] if n%2 else top[::-1]
    return top + bottom

