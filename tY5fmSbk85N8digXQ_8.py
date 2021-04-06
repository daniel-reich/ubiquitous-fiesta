
def ones_infection(arr):
    coords = []
    r = 0
    c = 0
    for sarr in arr:
        for n in sarr:
            if n: coords.append((r, c))
            c += 1
        r += 1
        c = 0
    for coor in coords:
        r = arr[coor[0]]
        c = coor[1]
        for i,n in enumerate(r):
            r[i] = 1
        for sarr in arr:
            sarr[c] = 1
    return arr

