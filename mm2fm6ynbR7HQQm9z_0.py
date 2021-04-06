
def knights_jump(square):
    r, c, res = ord(square[0]) - 64, int(square[1]), []
    moves = ((-2, -1), (-1, -2), (-2, 1), (-1, 2), 
             (2, -1), (1, -2), (2, 1), (1, 2))
    for i, j in moves:
        if 1 <= r+i <= 8 and 1 <= c+j <= 8:
            res.append(chr(r+i+64) + str(c+j))         
    return ','.join(sorted(res, key=lambda x: (x[1], x[0])))

