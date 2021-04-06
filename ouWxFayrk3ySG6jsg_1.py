
ROWS = (16449, 257, 5121, 68, 20740, 1028, 4176, 272, 17424)
def who_won(board):
    s = sum(r for x, r in zip(sum(board,[]), ROWS) if x=='X')
    return 'X' if s & 21845 & s >> 1 else 'O'

