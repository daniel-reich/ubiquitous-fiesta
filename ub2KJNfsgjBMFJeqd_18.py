
from random import randint
​
​
class Game:
​
    def __init__(self, _rows=14, _cols=18, _mines=40):
        self.rows = _rows
        self.cols = _cols
        self.mines = _mines
        mine_locations, neighbors_count = Game.make_distribution(_rows,
                                                                 _cols,
                                                                 _mines)
        self.board = [[Cell(row, col, mine_locations[row][col] > 0,
                            neighbors_count[row][col])
                       for col in range(_cols)] for row in range(_rows)]
​
    @staticmethod
    def make_distribution(n_rows, n_cols, n_mines):
        res = [[0] * n_cols for _ in range(n_rows)]
        neighbors = [[0] * n_cols for _ in range(n_rows)]
        if n_mines > n_rows * n_cols:
            n_mines = n_rows * n_cols
        mine_idx = set()
        while len(mine_idx) < n_mines:
            mine_idx.add(randint(0, n_rows * n_cols - 1))
        mine_idx = sorted(mine_idx)
        for i in mine_idx:
            res[i // n_cols][i % n_cols] = 1
        for r_idx in range(n_rows):
            for c_idx in range(n_cols):
                neighbors[r_idx][c_idx] = sum(res[x][y] > 0 for x, y in
                                              [(r_idx + i, c_idx + j) for i, j
                                               in
                                               [(i, j) for i in range(-1, 2)
                                                for j in range(-1, 2) if
                                                i or j]]
                                              if 0 <= x < n_rows
                                              and 0 <= y < n_cols)
        return res, neighbors
​
​
class Cell:
​
    def __init__(self, _row=0, _col=0, _mine=False, _neighbors=0):
        self.row = _row
        self.col = _col
        self.mine = _mine
        self.flag = False
        self.open = False
        self.neighbors = _neighbors

