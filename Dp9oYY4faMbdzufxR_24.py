
def left_slide(row):
    n = len(row)
    if not sum(row): return row
    
    row = [x for x in row if x]
    
    a = [row[0]]
​
    for i,x in enumerate(row[1:], 1):
        if x == a[-1]:
            a[-1] = a[-1] + x
            a.append('-')
        else:
            a.append(x)
​
    d = [x for x in a if x != '-']
    return d + [0] * (n - len(d))

