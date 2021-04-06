
def minesweeper_numbers(board):
    all_places_to_visit = [(-1, -1), (-1, 1), (-1, 0), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)]
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] == 1:
                board[row][col] = 9
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] != 9:
                counter = 0
                for x, y in all_places_to_visit:
                    if 0 <= row+x < len(board) and 0 <= col+y < len(board[row]):
                        if board[row+x][col+y] == 9:
                            counter += 1
                board[row][col] = counter
    return board

