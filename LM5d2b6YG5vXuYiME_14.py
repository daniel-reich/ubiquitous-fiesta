
def can_enter_cave(x):
    W, H = len(x[0]), len(x)
    queue = [(r, 0) for r in range(H) if x[r][0] == 0]
    while len(queue) > 0:
        (row, col) = queue.pop(0)
        for row2, col2 in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
            if 0 <= row2 < H and 0 <= col2 < W and x[row2][col2] == 0:
                if col2 == W - 1:
                    return True
                queue.append((row2, col2))
                x[row2][col2] = 1
    return False

