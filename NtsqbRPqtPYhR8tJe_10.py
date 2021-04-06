
def blocks(b):
    add = 7
    if b == 0:
        return 0
    if b == 1:
        return 5
    return blocks(b-1) + add + b-2

