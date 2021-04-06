
import copy
def game_of_life(board):
    board_copy = copy.deepcopy(board)
    string = ''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0:
                if j == 0:
                    total = sum(board[i][:j+2]) + sum(board[i+1][:j+2])
                elif j == len(board[0])-1:
                    total = sum(board[i][j-1:]) + sum(board[i+1][j-1:])
                else:
                    total = sum(board[i][j-1:j+2]) + sum(board[i+1][j-1:j+2])
            elif i == len(board)-1:
                if j == 0:
                    total = sum(board[i-1][:j+2]) + sum(board[i][:j+2])
                elif j == len(board[0])-1:
                    total = sum(board[i-1][j-1:]) + sum(board[i][j-1:])
                else:
                    total = sum(board[i-1][j-1:j+2]) + sum(board[i][j-1:j+2])
            elif j == 0 and i != 0 and i != len(board)-1:
                total = sum(board[i-1][:j+2]) + sum(board[i][:j+2]) + sum(board[i+1][:j+2])
            elif j == len(board[0])-1 and i != 0 and i != len(board)-1:
                total = sum(board[i-1][j-1:]) + sum(board[i][j-1:]) + sum(board[i+1][j-1:])
            else:
                total = sum(board[i-1][j-1:j+2]) + sum(board[i][j-1:j+2]) + sum(board[i+1][j-1:j+2])
​
            if board_copy[i][j] == 0:
                if total == 3:
                    board_copy[i][j] = 1
            else:
                if total == 1 or total == 2 or total > 4:
                    board_copy[i][j] = 0
​
            string += str(board_copy[i][j])
        string += '\n'
    string = string.replace('0', '_')
    string = string.replace('1', 'I')
    return string[:-1]

