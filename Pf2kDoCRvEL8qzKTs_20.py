
def order_people(shape, n):
    if n > shape[0] * shape[1]:
        return 'overcrowded'
    line, row, rownum = [], [], 1
    for i in range(1, shape[0] * shape[1] + 1):
        if i <= n:
            if rownum % 2 == 0:
                row.insert(0, i)
            else:
                row += [i]
        else:
            if rownum % 2 == 0:
                row.insert(0, 0)
            else:
                row += [0]
        if (i % shape[1] == 0):
            line += [row]
            row = []
            rownum += 1
​
    return line

