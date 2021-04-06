
BIN = (16449, 68, 4176, 257, 20740, 272, 5121, 1028, 17424)
​
def x_and_o(board):
    brd = tuple(zip(range(9), '|'.join(board)[::2], BIN))
    brdsum = sum(s for i,c,s in brd if c=='X')
    for i,c,s in brd:
        if c == ' ' and 2*s & brdsum:
            return [i//3 + 1, i%3 + 1]
    return False

