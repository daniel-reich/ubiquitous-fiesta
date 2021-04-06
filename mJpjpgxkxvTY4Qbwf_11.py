
def bingo_check(brd):
    return any(row == ['x']*5 for row in brd) or \
           any(row == ('x',)*5 for row in zip(*brd)) or \
           all(brd[i][i] == 'x' for i in range(5)) or \
           all(brd[i][4-i] == 'x' for i in range(5))

