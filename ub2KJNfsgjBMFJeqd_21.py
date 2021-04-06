
import random
​
​
class Game:
    def __init__(self, rows=14, cols=18, mines=40):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        
        number_of_cells = rows * cols
        number_of_False_cells = number_of_cells - mines
        
        boolean_frequencies = []
        for mine in range(mines):
            boolean_frequencies.append(True)
        
        for x in range(number_of_False_cells):
            boolean_frequencies.append(False)
        
        random.shuffle(boolean_frequencies)
        
        board = []
        for y in range(rows):
            row_list = []
            for x in range(cols):
                true_or_false = boolean_frequencies[-1]
                boolean_frequencies.pop()
                row_list.append(Cell(y, x, true_or_false))
            board.append(row_list)
        
        self.board = board
        
        for y in range(rows):
            for x in range(cols):
                total_neighbors = 0
                for nbr_row in [y-1, y, y+1]:
                    for nbr_col in [x-1, x, x+1]:
                        if nbr_row == y and nbr_col == x:
                            continue
                        if 0 <= nbr_row < rows and 0 <= nbr_col < cols:
                            if self.board[nbr_row][nbr_col].mine:
                                total_neighbors += 1
                self.board[y][x].neighbors = total_neighbors
                
                
  
class Cell:
    def __init__(self, row=0, col=0, mine=False, flag=False, Open=False):
        self.row = row
        self.col = col
        self.mine = mine
        self.flag = flag
        self.open = Open
        self.neighbors = 1

