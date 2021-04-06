
class Sudoku:
    
    def __init__(self, digits):
        self.board = [[int(i) for i in digits[i:i+9]] for i in range(0, 81, 9)]
        self.columns = [list(i) for i in zip(*self.board)]
        self.squares = [self.board[i][j:j+3] + self.board[i+1][j:j+3] + self.board[i+2][j:j+3] for i in (0, 3, 6) for j in (0, 3, 6)]
        
    def get_row(self, r):
        return self.board[r]
    
    def get_col(self, c):
        return self.columns[c]
    
    def get_sqr(self, a, b=False):
        return self.squares[a] if not b else self.squares[a//3*3 + b//3]

