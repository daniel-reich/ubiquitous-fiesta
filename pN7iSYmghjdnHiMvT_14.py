
class Battleship:
  def __init__(self, scheme, target):
    self.scheme = scheme
    self.target = target
    self._board = [[' '] * 5 for _ in range(5)]
    self.coord = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    self._hits = list()
​
  def board(self):
    for x, y in self.scheme: self._board[self.coord[x]][int(y)-1] = 's'
    self.hits()
    return self._board
​
  def hits(self):
    self._hits = [x for x in self.scheme if x in self.target]
    for x, y in self._hits: self._board[self.coord[x]][int(y) - 1] = 'X'
    m = filter(lambda x: x not in self._hits, self.target)
    for x, y in m: self._board[self.coord[x]][int(y) - 1] = '.'
    return len(self._hits)
​
  def sunk(self):
    v, h = sorted(self._hits, key=lambda x: x[0]), sorted(self._hits, key=lambda x: x[1])
    return sum(v[i][0] == x and abs(int(v[i][1]) - int(y)) == 1 for i, (x, y) in enumerate(v[1:])) \
           + sum(h[i][1] == y and abs(ord(h[i][0]) - ord(x)) == 1 for i, (x, y) in enumerate(h[1:]))
​
  def points(self):
    return self.hits() + (self.sunk() << 1)

