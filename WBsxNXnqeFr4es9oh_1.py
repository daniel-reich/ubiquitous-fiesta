
from math import ceil
def make_cycle(s, n):
    side, res = [s + i * 4 for i in range(n - 1)], []
    for _ in range(4):
        res.append(side)
        side = [x + 1 for x in side]
    return res
​
def make_square(size):
    res, s = [[0] * size for _ in range(size)], 1
    for i in range(size // 2):
        len_edge = size - i * 2
        lst_nums = make_cycle(s, len_edge)
        for idx, v in enumerate(lst_nums[0]):
            res[i][i + idx] = v
        for idx, v in enumerate(lst_nums[1]):
            res[i + idx][i + len_edge - 1] = v
        for idx, v in enumerate(lst_nums[2]):
            res[i + len_edge - 1][i + len_edge - 1 - idx] = v
        for idx, v in enumerate(lst_nums[3]):
            res[i + len_edge - 1 - idx][i] = v
        s += (len_edge - 1) * 4
    if size % 2:
        center = (size - 1) // 2
        res[center][center] = size * size
    return res
​
def clockwise_cipher(msg):
    len_msg = len(msg)
    square_size = ceil(pow(len_msg, 0.5))
    msg = " {}{}".format(msg, (square_size * square_size - len_msg) * " ")
    idx_square = make_square(square_size)
    res = [[msg[col] for col in row] for row in idx_square]
    return "".join("".join(row) for row in res)

