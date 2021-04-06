
def cannot_capture(board):
    knights = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 1:
                knights.append((row, col))
    for i in range(len(knights)):
        row1, col1 = knights[i]
        for j in range(i + 1, len(knights)):
            row2, col2 = knights[j]
            if sorted([abs(row1 - row2), abs(col1 - col2)]) == [1, 2]:
                return False
    return True

