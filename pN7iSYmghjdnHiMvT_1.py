
class Battleship:
    def __init__(self,scheme,guesses):
        self.scheme=scheme
        self.guesses=guesses
        scheme = set(self.scheme[:])
        guesses = set(self.guesses[:])
        self.inter = list(scheme.intersection(guesses))
    def board(self):
        boarder=[]
        counter=-1
        alphabe=["A","B","C","D","E"]
        scheme=set(self.scheme[:])
        guesses=set(self.guesses[:])
        scheme=list(scheme)
        guesses=list(guesses)
        for i in self.inter:
            scheme.remove(i)
            guesses.remove(i)
        for i in alphabe:
            counter+=1
            boarder.append([])
            for j in range(1,6):
                if i+str(j) in guesses:
                    boarder[counter].append(".")
                elif i+str(j) in scheme:
                    boarder[counter].append("s")
                elif i+str(j) in self.inter:
                    boarder[counter].append("X")
                else:
                    boarder[counter].append(" ")
        return boarder
    def hits(self):
        return len(self.inter)
    def sunk(self):
        summer=0
        for i in range(0,len(self.inter)-1):
            for j in range(i+1,len(self.inter)):
                if abs(int(self.inter[i][1])-int(self.inter[j][1]))==1 and self.inter[i][0] ==self.inter[j][0]:
                    summer+=1
                if abs(ord(self.inter[i][0])- ord(self.inter[j][0]))==1 and self.inter[i][1] == self.inter[j][1]:
                    summer+=1
        return summer
    def points(self):
        return  len(self.inter) + self.sunk()*2

