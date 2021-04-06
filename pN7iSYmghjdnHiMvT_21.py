
class Battleship:
    def __init__(self, scheme, guesses):
        self.scheme = scheme
        self.guesses = guesses
        self.__d_board = [[" " for j in range(5)] for i in range(5)]
​
    def board(self):
        ships = self.__d_board
        for c in self.scheme:
            i,j = ord(c[0])-65, int(c[1])-1
            ships[i][j] = "s"
​
        board = ships
        for g in self.guesses:
            i,j = ord(g[0])-65, int(g[1])-1
            if board[i][j] == "s":
                board[i][j] = "X"
            else:
                board[i][j] = "."
​
        return board
​
​
    def hits(self):
        board = self.board()
        return sum(l.count('X') for l in board)
​
    def sunk(self):
        board = self.board()
        sunk_count = 0
        for s in board:
            if "XX" in ''.join(s) and ''.join(s).count("XX")==1:
                sunk_count += 1
            elif "XX" in ''.join(s) or "XXXX" in ''.join(s):
                sunk_count+=2
​
        for s in list(zip(*board)):
            if "XX" in ''.join(s) and ''.join(s).count("XX")==1:
                sunk_count += 1
            elif "XX" in ''.join(s) or "XXXX" in ''.join(s):
                sunk_count+=2
        return sunk_count
​
    def points(self):
        sunk_count = self.sunk()
        hit_count = self.hits()
        return hit_count + 2*sunk_count

