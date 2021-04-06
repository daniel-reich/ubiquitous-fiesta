
def where_is_waldo(lst):
    row, col = 0, 0
    for i in lst:
        row += 1
        col = 0
        for x in range(len(i) - 1):
            col += 1
            if i[x] == i[x + 1]:
                continue
            try:
                if i[x+1] == i[x+2]:
                    return [row, col]
            except:
                if i[x+1] == i[x-1]:
                    return [row, col]
            col +=1
            return [row, col]

