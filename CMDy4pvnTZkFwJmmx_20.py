
class Sudoku:
    def __init__(self, num_str):
        self.board = []
        a = -9
        for i in range(9):
            a += 9
            self.board.append([])
            for j in range(a, a + 9):
                self.board[i].append(int(num_str[j]))
​
    def get_row(self, n):
        return self.board[n]
​
    def get_col(self, n):
        return [self.board[k][n] for k in range(0, 9)]
​
    def get_sqr(self, n, m=-1):
        if m == -1:
            m1 = (n % 3) * 3
            n1 = (n // 3) * 3
        else:
            n1 = (n // 3) * 3
            m1 = (m // 3) * 3
        return [self.board[j][k] for j in range(n1, n1 + 3) for k in range(m1, m1 + 3)]

