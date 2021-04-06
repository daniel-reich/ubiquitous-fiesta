
from itertools import combinations
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
letters = "ABCDE"
def row(string):
  return letters.index(string[0])
def col(string):
  return int(string[1]) - 1
def is_pair(p1,p2):
  if p1 == p2:
    return False
  else:
    return abs(row(p1) - row(p2)) <= 1 and abs(col(p1)-col(p2)) <= 1
def pairs(lst):
  return list(filter(lambda x: is_pair(x[0],x[1]),list(combinations(lst,2))))
class Battleship:
  def __init__(self, scheme, guesses):
    self.scheme = scheme
    self.guesses = guesses
​
  def board(self):
    grid = [[' ' for j in range(0,5)] for i in range(0,5)]
    for s in self.scheme:
      grid[row(s)][col(s)] = "s"
    for guess in self.guesses:
      if guess in self.scheme:
        grid[row(guess)][col(guess)] = "X"
      else:
        grid[row(guess)][col(guess)] = "."
    return grid
          
  def hits(self):
    return sum(list(map(lambda x: x.count("X"),self.board())))
​
  def sunk(self):
    p = 0
    for combo in pairs(self.guesses):
      if combo in pairs(self.scheme):
        p += 1
    return p
​
  def points(self):
    return self.hits() + 2 * self.sunk()

