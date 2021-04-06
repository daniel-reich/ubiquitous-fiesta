
# CHARACTERS SET
# " " -> blank
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
  def __init__(self, scheme, guesses):
    self.b = [[' ' for _ in range(5)] for _ in range(5)]
    self.h = 0
    for s in scheme:
      i,j = 'ABCDE'.index(s[0]), '12345'.index(s[1])
      if s in guesses: 
        self.b[i][j] = 'X'
        self.h+=1
      else: self.b[i][j] = 's'
    for g in guesses:
      i,j = 'ABCDE'.index(g[0]), '12345'.index(g[1])
      if g not in scheme: self.b[i][j] = '.'
    
    self.c = {tuple(sorted({s1,s2})) for s1 in scheme for s2 in scheme if adj(s1,s2)}
    
    self.s = sum(1 for c in self.c if all(s in guesses for s in c))
​
  def board(self):
    return self.b
​
  def hits(self):
    return self.h
​
  def sunk(self):
    return self.s
​
  def points(self):
    return self.h + 2*self.s
​
def adj(s1,s2):
  return abs('ABCDE'.index(s1[0]) - 'ABCDE'.index(s2[0])) +\
         abs('12345'.index(s1[1]) - '12345'.index(s2[1])) == 1

