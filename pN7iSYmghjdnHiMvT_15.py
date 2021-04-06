
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
    def __init__(self, scheme, guesses):
        letters ="ABCDE"
        self.scheme = [(letters.index(pos[0]),int(pos[1])-1) for pos in scheme]
        self.guesses = [(letters.index(pos[0]),int(pos[1])-1) for pos in guesses]
​
    def board(self):
        board = []
        for i in range(5):
            line = []
            for j in range(5):
                if (i,j) in self.scheme:
                    if (i,j) in self.guesses:
                        line.append("X")
                    else:
                        line.append("s")
                else:
                    if (i,j) in self.guesses:
                        line.append(".")
                    else:
                        line.append(" ")
            board.append(line)
            print(line)
        return board
​
    def hits(self):
        total = 0
        for i in range(5):
            for j in range(5):
                if (i,j) in self.scheme and (i,j) in self.guesses:
                    total += 1
        return total
​
    def sunk(self):
        total = 0
        for i in range(4):
            for j in range(4):
                if (((i,j) in self.scheme and (i,j) in self.guesses) and
                        (((i+1,j) in self.scheme and (i+1,j) in self.guesses)
                        or ((i,j+1) in self.scheme and (i,j+1) in self.guesses))):
                    total += 1
        for i in range(4):
            if (i,4) in self.scheme and (i,4) in self.guesses and (i+1,4) in self.scheme and (i+1,4) in self.guesses:
                total += 1
        for j in range(4):
            if (4,j) in self.scheme and (4,j) in self.guesses and (4,j+1) in self.scheme and (4,j+1) in self.guesses:
                total += 1
​
        return total
​
    def points(self):
        return self.hits()+ 2*self.sunk()

