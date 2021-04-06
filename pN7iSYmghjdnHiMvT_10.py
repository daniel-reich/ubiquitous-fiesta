
DXDY = ((-1,0), (1,0), (0,-1), (0,1))
def getyx(cd):
    return 'ABCDE'.index(cd[0]), int(cd[1])-1
​
class Battleship:
    def __init__(self, scheme, guesses):
        brd = [[' ']*5 for i in '12345']
        for y, x in (getyx(cd) for cd in scheme):
            brd[y][x] = 's'
        self.hit = 0
        self.snk = 0
        for y, x in (getyx(cd) for cd in guesses):
            if brd[y][x] == 's':
                brd[y][x] = 'X'
                self.hit += 1
                if any(brd[y+dy][x+dx] == 'X' for dx,dy in DXDY \
                         if 0<=x+dx<5 and 0<=y+dy<5):
                    self.snk += 1
            else:
                brd[y][x] = '.'
        print(*brd, sep='\n')
        self.brd = brd
        
    def board(self):
        return self.brd
​
    def hits(self):
        return self.hit
​
    def sunk(self):
        return self.snk
​
    def points(self):
        return self.hit + 2*self.snk

