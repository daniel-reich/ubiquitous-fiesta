
def block_player(a, b):
    a_row, a_col = a // 3, a % 3
    b_row, b_col = b // 3, b % 3
    d_1, d_2 = {0, 4, 8}, {2, 4, 6}
    if a_row == b_row:
        return a_row * 3 + 3 - a_col - b_col
    elif a_col == b_col:
        return (3 - a_row - b_row) * 3 + a_col
    elif a in d_1 and b in d_1:
        return (d_1 - {a} - {b}).pop()
    elif a in d_2 and b in d_2:
        return (d_2 - {a} - {b}).pop()

