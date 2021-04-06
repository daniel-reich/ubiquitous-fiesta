
def left_slide(row):
    if sum(row) == 0:
        return row
    L = len(row)
    row = [e for e in row if e > 0]
    last = row.pop(0)
    new_row = []
    while len(row) > 0:
        cur = row.pop(0)
        if last == cur:
            new_row.append(last + cur)
            last = 0
        else:
            new_row.append(last)
            last = cur
    if last > 0:
        new_row.append(last)
    row = [e for e in new_row if e > 0]        
    row = row + [0] * (L - len(row))
    return row

