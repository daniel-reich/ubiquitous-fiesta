
def left_slide(row):
    count0 = row.count(0)
    for i in range(count0):
        row.remove(0)
        row.append(0)
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            row[i] += row[i+1]
            row[i+1] = 0
    count0 = row.count(0)
    for i in range(count0):
        row.remove(0)
        row.append(0)
    return row

