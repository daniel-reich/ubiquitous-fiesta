
class Sudoku:
​
    n_edge = 9
    n_sqr = 3
​
    def __init__(self, s):
        self.original_str = s
        self.board = []
        self._make_board_()
​
    def _make_board_(self):
        for r in range(Sudoku.n_edge):
            row = [int(self.original_str[c])
                   for c in range(r * Sudoku.n_edge, (r + 1) * Sudoku.n_edge)]
            self.board.append(row)
​
    def get_row(self, row):
        return self.board[row]
​
    def get_col(self, col):
        return [self.board[r][col] for r in range(Sudoku.n_edge)]
​
    def _get_mini_sqr_(self, begin_row, begin_col):
        return [self.board[r][c]
                for r in range(begin_row, begin_row + Sudoku.n_sqr)
                for c in range(begin_col, begin_col + Sudoku.n_sqr)]
​
    def get_sqr(self, *args):
        row = args[0] // Sudoku.n_sqr
        col = args[0] % Sudoku.n_sqr
        if len(args) == 2:
            col = args[1] // Sudoku.n_sqr
        return self._get_mini_sqr_(row * Sudoku.n_sqr, col * Sudoku.n_sqr)

