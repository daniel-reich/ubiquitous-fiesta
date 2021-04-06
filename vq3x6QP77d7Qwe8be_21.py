
def odd_square_patch(lst):
    size, r, w, h = 0, 0, len(lst[0]), len(lst)
    while r < h - size:
        c = 0
        while c < w - size:
            d = 0
            while r + d < h and c + d < w:
                ext = [(r+d,x) for x in range(c, c+d+1)] + [(y,c+d) for y in range(r,r+d)]
                if not all(lst[i][j]%2 for i,j in ext):
                    break
                d += 1
                if d > size:
                    size = d
            c += 1
        r += 1
    return size

