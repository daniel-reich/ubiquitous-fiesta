
def block(lst):
    store = 0
    for i in range(len(lst)):
        for x in range(len(lst[i])):
            if lst[i][x] >1:
                for y in range(i+1,len(lst)):
                    store +=lst[y][x]
    return store

