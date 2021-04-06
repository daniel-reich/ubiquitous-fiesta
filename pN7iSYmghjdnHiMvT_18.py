
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
​
    def __init__(self, scheme, guesses):
        self._board = [[' ' for _ in range(5)] for __ in range(5)]
        # place ships:
        for s in scheme:
            row, col = self._get_coordinates(s)
            self._board[row][col] = 's'
        # identify patrols and cruisers:
        self.patrols = []
        self.cruisers = []
        for row in range(5):
            for col in range(5):
                if self._board[row][col] == ' ':
                    continue
                if row < 4 and self._board[row+1][col] == 's':
                    self.cruisers.append([[row, col], [row+1, col]])
                elif col < 4 and self._board[row][col+1] == 's':
                    self.cruisers.append([[row, col], [row, col+1]])
                else:
                    self.patrols.append([row, col])
        for c in self.cruisers:
            for row, col in c:
                if [row, col] in self.patrols:
                    self.patrols.remove([row, col])
        # analyze guesses:
        self._hits = 0
        self._points = 0
        self._sunk = 0
        for g in guesses:
            row, col = self._get_coordinates(g)
            if self._board[row][col] == ' ':
                self._board[row][col] = '.'
            else:
                if [row, col] in self.patrols:
                    # hit a patrol
                    self._board[row][col] = 'X'
                    self._points += 1
                    self._hits += 1
                    self.patrols.remove([row, col])
                elif self._board[row][col] == 's':
                    # hit a cruiser:
                    self._board[row][col] = 'X'
                    self._points += 1
                    self._hits += 1
                    for i in range(len(self.cruisers)):
                        if [row, col] in self.cruisers[i]:
                            self.cruisers[i].remove([row, col])
                            if len(self.cruisers[i]) == 0:
                                self._points += 2
                                self._sunk += 1
                                self.cruisers.pop(i)
                            break
                         
    def _get_coordinates(self, s):
        return ord(s[0]) - 65, int(s[1]) - 1
    
    def board(self):
        return self._board
    
    def hits(self):
        return self._hits
​
    def sunk(self):
        return self._sunk
​
    def points(self):
        return self._points

