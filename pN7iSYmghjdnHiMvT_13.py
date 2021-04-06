
class Battleship:
    def __init__(self, s, g):
        dic = {i[1] + str(j+1): j + 5 * i[0]\
               for i in enumerate("ABCDE") for j in range(5)}
        self.s = {dic[i]:True for i in s}
        self.g = {dic[i]:True for i in g}
        pass
​
    def board(self):
        boar = ["X" if (i in self.s)*(i in self.g) else "s" if i in self.s\
                        else "." if i in self.g else " " for i in range(25)]
        return [boar[i:i+5] for i in range(0,21,5)]
​
    def hits(self):
        return sum([i in self.s for i in self.g])
​
    def sunk(self):
        hit = set([i if i in self.s else -2 for i in self.g])
        return sum([1 if (j+1)%5 and (j+1 in hit or j+5 in hit) else 1\
                        if not (j+1)%5 and j+5 in hit else 0 for j in hit])
​
    def points(self):
        return self.hits() + 2*self.sunk()

