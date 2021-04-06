
def minesweeper_numbers(board):
    result = []
    for r in range(0,len(board)):
        row = []
        for i in range(0,len(board[r])):
            if board[r][i] == 1:
                row.append(9)
            else:
                counter = 0
                if r != 0 and board[r-1][i] == 1:
                    counter += 1
                if r != len(board)-1 and board[r+1][i] == 1:
                    counter += 1
                if r != 0 and i != 0 and board[r-1][i-1] == 1:
                    counter += 1
                if r != 0 and i != len(board[r])-1 and board[r-1][i+1] == 1:
                    counter += 1
                if r != len(board)-1 and i != 0 and board[r+1][i-1] == 1:
                    counter += 1
                if r != len(board)-1 and i != len(board[r])-1 and board[r+1][i+1] == 1:
                    counter += 1
                if i != 0 and board[r][i-1] == 1:
                    counter += 1
                if i != len(board[r])-1 and board[r][i+1] == 1:
                    counter += 1
                row.append(counter)
        result.append(row)
    return result

