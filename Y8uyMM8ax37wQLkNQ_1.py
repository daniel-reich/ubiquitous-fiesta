
def matrix(n):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = [[0] * n for _ in range(n)]
    pos, dir_idx = [0, 0], 0
    for val in range(1, pow(n, 2) + 1):
        res[pos[0]][pos[1]] = val
        add_idx = direction[dir_idx % 4]
        if not (0 <= pos[0] + add_idx[0] < n and 0 <= pos[1] + add_idx[1] < n
                and res[pos[0] + add_idx[0]][pos[1] + add_idx[1]] == 0):
            dir_idx += 1
            add_idx = direction[dir_idx % 4]
        pos = [pos[0] + add_idx[0], pos[1] + add_idx[1]]
    return res

