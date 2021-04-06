
class Sudoku:
    def __init__(self, st):
        self.brd = [int(d) for d in st]
        self.board = [self.brd[i:i+9] for i in range(0,81,9)]
​
    def get_row(self, n):
        return self.board[n]
​
    def  get_col(self, n):
        return self.brd[n::9]
​
    def get_sqr(self, n, m=None):
        if m == None:
            i0 = n//3*27 + n%3*3
        else:
            i0 = (n-n%3) * 9 + m-m%3
        return [self.brd[i0+i] for i in (0,1,2,9,10,11,18,19,20)]

