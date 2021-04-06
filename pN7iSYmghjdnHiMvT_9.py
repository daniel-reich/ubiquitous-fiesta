
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
    def __init__(self, scheme, guesses):
        self.scheme = scheme
        self.guesses = guesses
​
    def board(self):
        row = "ABCDE"
        ro = {r + str(y + 1): (x, y)  for x, r in enumerate(row) for y in range(5)}
        mtx = [[" " for x in range(5)] for i in range(5)] 
​
        for i in self.scheme:
            x, y = ro[i]
            mtx[x][y] = "X" if i in self.guesses else "s"
         
        for i in self.guesses:
            x, y = ro[i]
            if i not in self.scheme:
                mtx[x][y] = "."
        
        return mtx
​
​
    def hits(self):
        return sum(i.count("X") for i in self.board())
​
    def sunk(self):
        val = self.board()
        hor = sum(True for i in val for x in range(4) if "X" in i[x] if i[x] in i[x+1])
        ver = sum(True for i in range(4) for x in range(5) if "X" in val[i][x] if val[i][x] in val[i+1][x])
        return hor + ver
​
    def points(self):
        return self.hits() + self.sunk() * 2

