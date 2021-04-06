
class Battleship:
    def _setcell(self, loc, val):
        self.scheme[ord(loc[0]) - ord('A')][int(loc[1]) - 1] = val
​
    def _getCell(self, loc):
        return self.scheme[ord(loc[0]) - ord('A')][int(loc[1]) - 1]
​
    def __init__(self, scheme, input):
        self.scheme = [[' ' for i in range(5)] for j in range(5)]
        for loc in scheme:
            self._setcell(loc, 's')
        self.score = { 'hits': 0, 'sunk': 0, 'points': 0 }
        for loc in input:
            self._setcell(loc, 'X' if self._getCell(loc) == 's' else '.')
        for r in range(5):
            for c in range(5):
                if self.scheme[r][c] == 'X':
                    self.score['hits'] += 1
                    self.score['points'] += 1
                    if (r < 4 and self.scheme[r+1][c] == 'X') or (c < 4 and self.scheme[r][c+1] == 'X'):
                        self.score['sunk'] += 1
                        self.score['points'] += 2                       
    def board(self):
        return self.scheme    
    def hits(self):
        return self.score['hits']       
    def sunk(self):
        return self.score['sunk']    
    def points(self):
        return self.score['points']

