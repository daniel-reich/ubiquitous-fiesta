
def index_converter(indexes):
    alph = "ABCDE"
    nums = "12345"
    real_indexes = []
    for index in indexes:
        row = alph.index(index[0])
        column = nums.index(index[1])
​
        real_indexes.append([row, column])
    return real_indexes
​
class Battleship:
    def __init__(self, scheme, guesses):
        self.scheme = index_converter(scheme)
        self.guesses = index_converter(guesses)
​
    def board(self, return_hits=False):
        matrix = []
        hits = 0
        for row in range(5):
            lst = []
            for column in range(5):
                if [row, column] in self.scheme and [row, column] in self.guesses:
                    lst.append("X")
                    hits += 1
                elif [row, column] in self.scheme and not [row, column] in self.guesses:
                    lst.append("s")
                elif not [row, column] in self.scheme and [row, column] in self.guesses:
                    lst.append(".")
                else:
                    lst.append(" ")
            matrix.append(lst)
        if return_hits:
            return hits
        return matrix
​
    def hits(self):
        return self.board(True)
​
    def sunk(self):
        board = self.board()
        sunk = 0
        sunkships = []
        for i in board:
            if "XX" in "".join(i):
                sunk += 1
        for row in range(len(board)):
            for column in range(row + 1):
                if board[row][column] == "X" and not [row, column] in sunkships:
                    if row + 1 < 5 and board[row + 1][column] == "X":
                        sunk += 1
                        sunkships.append([row, column])
                        sunkships.append([row + 1 , column])
        return sunk
​
    def points(self):
        return self.hits() + (self.sunk() * 2)

