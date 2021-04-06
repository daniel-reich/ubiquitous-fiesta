
import random
​
class Game:
    def __init__(self, r = 14, c = 18, m = 40):
        def init_board(r, c, m):
            bb = []
            idx_mine = random.sample(range(r*c), m)
            for i in range(r):
                bb.append([])
                for j in range(c):
                    bb[i].append(Cell(i, j, (i*c)+j in idx_mine))
            
            def update_neighbor(board, cell):
                n, r, c = cell.neighbors, cell.row, cell.col
                
                if not r and not c:
                    for row in board[r:r+2]:
                        for col in row[c:c+2]:
                            if col.row == cell.row and col.col == cell.col:
                                continue
                            n += col.mine
                    return n
                    
                if not r and c:
                    for row in board[r:r+2]:
                        for col in row[c-1:c+2]:
                            if col.row == cell.row and col.col == cell.col:
                                continue
                            n += col.mine
                    return n
                
                if r and not c:
                    for row in board[r-1:r+2]:
                        for col in row[c:c+2]:
                            if col.row == cell.row and col.col == cell.col:
                                continue
                            n += col.mine
                    return n
                
                if r and c:
                    for row in board[r-1:r+2]:
                        for col in row[c-1:c+2]:
                            if col.row == cell.row and col.col == cell.col:
                                continue
                            n += col.mine
                    return n
​
            def display(cell):
                if cell.mine: return 9
                if cell.neighbors: return cell.neighbors
                if cell.open: return cell.neighbors
                if cell.flag: return 'F'
                return 0
            
            for row in bb:
                for cell in row:
                    cell.neighbors = update_neighbor(bb, cell)
                    cell.display = display(cell)
                    
            return bb
        
        self.rows = r
        self.cols = c
        self.mines = m
        self.bb = init_board(self.rows, self.cols, self.mines)
        self.board = self.bb
        
    def show_board(self):
        rows = []
        for i, row in enumerate(self.board):
            rows.append([])
            for j, col in enumerate(row):
                rows[i].append(col.display)
                
        for line in rows:
            print(line)
                    
​
​
class Cell():
    def __init__(self, r, c, m):
        self.row = r
        self.col = c
        self.mine = m
        self.flag = False
        self.open = False
        self.neighbors = 0
        self.display = 0

