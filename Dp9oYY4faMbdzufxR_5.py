
def left_slide(row):
    if sum(row) == 0:
        return [0,0,0,0]
​
    chk = True
    while chk:
        chk = False
        if row[0] == 0:
            chk = True
            del row[0]
            row.append(0)
    a = 0
    b = 1
    while b < len(row):
        if row[b] == 0:
            del row[b]
            row.append(0)
        if row[a] == row[b]:
            row[a] = row[a]*2
            del row[b]
            row.append(0)
        a += 1
        b += 1
​
    return row

