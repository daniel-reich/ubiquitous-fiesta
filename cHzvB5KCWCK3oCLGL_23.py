
def game_of_life(board):
    output = [['_' for a in range(len(board[0]))] for b in range(len(board))]
    output_string = ''
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighbors = 0
            for k in range(max(0, i - 1), min(len(board), i + 2)):
                for l in range(max(0, j - 1), min(len(board[k]), j + 2)):
                    if i == k and j == l:
                        continue
                    neighbors += board[k][l]
            if board[i][j] == 1:
                if neighbors in (2, 3):
                    output[i][j] = 'I'
            else:
                if neighbors == 3:
                    output[i][j] = 'I'
    return '\n'.join([output_string + ''.join(k) for k in output])

