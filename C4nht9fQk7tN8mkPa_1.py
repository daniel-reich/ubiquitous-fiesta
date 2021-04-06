
def cannot_capture(board):
    def has_kills(row, col):
        attack_directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)] 
        return any(board[row+dy][col+dx] for dy,dx in attack_directions if 0<=row+dy<8 and 0<=col+dx<8)
    return not any(has_kills(row, col) for row in range(8) for col in range(8) if board[row][col])

