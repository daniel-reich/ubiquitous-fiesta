
def left_slide(row):
    global merged
    merged = []    
    for i in range(1, len(row)):
        move_one(i, row)
    return row
​
def move_one(j, r):
    global merged
    while j > 0:
        if r[j] == 0:
            return
        if r[j-1] == 0:
            r[j-1] = r[j]
            r[j] = 0
            j = j - 1
        elif (r[j-1] == r[j]) and (j-1 not in merged):
            r[j-1] = r[j-1] * 2
            r[j] = 0
            merged.append(j-1)
            return
        else:
            return

