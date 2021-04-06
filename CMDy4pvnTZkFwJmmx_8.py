
class Sudoku:
​
    def __init__(self, s):
        self.board = []
        for r in range(9):
            self.board.append([int(_) for _ in s[9*r:9*r+9]])
​
    def get_row(self, n):
        return self.board[n]
​
    def get_col(self, n):
        return [list(i) for i in zip(*self.board)][n]
​
    def get_sqr(self, n, m=None):
        if m == None:
            row1 = 3 * (n // 3)
            col1 = 3 * (n % 3)
        else:
            row1 = 3 * (n // 3)
            col1 = 3 * (m // 3)
        ans = []
        for row in range(row1, row1 + 3):
            ans += self.board[row][col1:col1+3]
        return ans

