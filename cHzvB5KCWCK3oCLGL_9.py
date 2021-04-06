
import numpy as np
​
​
def game_of_life(board):
    def convolution(matrix, kernel):  # padded w/ 0 to handle edge cases
        matrixWithBorder = np.pad(matrix, ([1, 1], [1, 1]), mode="constant")
        rows, cols = matrix.shape
        matrixNew = np.zeros(matrix.shape)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                slice = matrixWithBorder[(i - 1):(i + 2), (j - 1):(j + 2)]
                matrixNew[i - 1, j - 1] = np.sum(kernel * slice).astype(int)
        return matrixNew
​
    board = np.array(board)
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]])
    neighbors = convolution(board, kernel)
    rows, cols = board.shape
    for i in range(rows):
        for j in range(cols):
            if board[i, j]:
                board[i, j] = 1 if 2 <= neighbors[i, j] <= 3 else 0
            else:
                board[i, j] = 1 if neighbors[i, j] == 3 else 0
​
    return str(board).translate(str.maketrans("01", "_I", " []"))

