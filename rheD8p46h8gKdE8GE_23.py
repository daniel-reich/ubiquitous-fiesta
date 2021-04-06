
def grayscale(lst):
    byte = lambda x: max(0, min(255, x))
    gray = lambda c: [sum(map(byte, c), 1) // 3] * 3
    return [[gray(pix) for pix in row] for row in lst]

