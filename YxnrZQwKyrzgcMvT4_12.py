
def rotate_transform(M, num):
    if abs(num) % 4 == 0:
        return M
    if num > 0:
        for _ in range(num % 4):
            M = [row[::-1] for row in [list(i) for i in zip(*M)]]
        return M
    return rotate_transform(M, 4-abs(num))

