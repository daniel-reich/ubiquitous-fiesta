
def make_dartboard(n):
    board = [[1 for _ in range(n)] for __ in range(n)]
    if n % 2 == 1:
        max_val = n // 2 + 1
        board[n // 2][n // 2] = max_val
        val = max_val - 1
        while val > 1:
            for row in [n // 2 - (max_val - val), n // 2 + (max_val - val)]:
                for col in range(n // 2 - (max_val - val), n // 2 + (max_val - val) + 1):
                    board[row][col] = val
            for col in [n // 2 - (max_val - val), n // 2 + (max_val - val)]:
                for row in range(n // 2 - (max_val - val), n // 2 + (max_val - val) + 1):
                    board[row][col] = val
            val -= 1    
    else:
        max_val = n // 2
        board[n // 2][n // 2] = max_val
        board[n // 2 - 1][n // 2] = max_val
        board[n // 2 - 1][n // 2 - 1] = max_val
        board[n // 2][n // 2 - 1] = max_val
        val = max_val - 1
        while val > 1:
            for row in [n // 2 - 1 - (max_val - val), n // 2 + (max_val - val)]:
                for col in range(n // 2 - 1 - (max_val - val), n // 2 + (max_val - val) + 1):
                    board[row][col] = val
            for col in [n // 2 - 1 - (max_val - val), n // 2 + (max_val - val)]:
                for row in range(n // 2 - 1 - (max_val - val), n // 2 + (max_val - val) + 1):
                    board[row][col] = val
            val -= 1    
    for i in range(n):
        board[i] = int(''.join(map(str, board[i])))
    return board

