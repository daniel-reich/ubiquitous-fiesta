
def minesweeper_numbers(board):
    new = [[0 for _ in range(len(board[0]))] for __ in range(len(board))]
    d = [-1, -1, -1, 0, 0, 1, 1, 1]
    e = [-1, 0, 1, -1, 1, -1, 0, 1]
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 1:
                new[r][c] = 9
            else:
                mines = 0
                for rr, cc in zip(d, e):
                        if -1 < r + rr < len(board) and -1 < c + cc < len(board[r]):
                            if board[r + rr][c + cc] == 1:
                                mines += 1
                new[r][c] = mines
    return new

