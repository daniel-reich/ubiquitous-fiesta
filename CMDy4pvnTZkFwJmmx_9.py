
class Sudoku:
    def __init__(self, board):
        
        self.board = [Sudoku.split(board[x:x+9]) for x in range(0, len(board), 9)]
​
    def split(word):
        return [int(char) for char in word]  
​
    def get_row(self, number):
        return self.board[number]
    def get_col(self, number):
        return [el[number] for el in self.board]
    
    def get_sqr(self, n, m=None):
        square = []
        brutBoard = sum(self.board, [])
        # for num in [0,3,6,27,30,54,57,60]:
        for i in range (0, len(brutBoard), 27):
            for num in range(i,i+9,3):
                if m is not None:
                    indexNumber = 9*n + m
                    if ((indexNumber>=num and indexNumber<=num+3) or (indexNumber>=num+9 and indexNumber<=num+12) or (indexNumber>=num+18 and indexNumber<=num+20)):
                        bigCellIs = brutBoard[num:num+3] + brutBoard[num+9:num+12] + brutBoard[num+18:num+21]
                        return bigCellIs
                square.append(brutBoard[num:num+3] + brutBoard[num+9:num+12] + brutBoard[num+18:num+21])
        return square[n]

