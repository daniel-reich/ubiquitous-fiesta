
def snakefill(n):
    length, idx = 1, 0
    area = n*n
    if n == 1: return 0
    while True:
        idx += 1
        length *= 2
        area -= length
        if area <= 0:
            return idx

