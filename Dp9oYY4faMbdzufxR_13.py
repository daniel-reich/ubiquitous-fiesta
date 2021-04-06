
def left_slide(row):
    x = []
    for n in row:
        x.append(0)
    
    for n in range(0, len(row)):
        if row[n] == 0:
            del row[n]
            row. append(0)
    
    for n in range(0, len(row)-1):
        if x[n] == 1:
            continue
        if row[n] == row[n + 1]:
            row[n] = row[n] + row[n + 1]
            row[n+1] = 0
            x[n + 1] = 1
    
    for n in range(0, len(row)):
        if row[n] == 0:
            del row[n]
            row. append(0)
            
    return row

