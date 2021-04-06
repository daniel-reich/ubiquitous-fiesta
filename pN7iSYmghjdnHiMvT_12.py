
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
    ret = ['']*5
    for i in range(5):
      ret[i]=[' ']*5
    a = 'ABCDE'
    n = '12345'
    for i in self.scheme:
      ret[a.index(i[0])][n.index(i[1])] = 's'
    for i in self.guesses:
      if ret[a.index(i[0])][n.index(i[1])] == 's':
        ret[a.index(i[0])][n.index(i[1])] = 'X'
      else:
        ret[a.index(i[0])][n.index(i[1])] = '.'
    return ret
​
  def hits(self):
    return len([i for i in self.guesses if i in self.scheme])
​
  def sunk(self):
    a = 'ABCDE'
    n = '12345'
    cruisers = []
    for i in self.scheme:
      ship = [i]
      for j in [x for x in self.scheme if x!=i]:
        if (i[0]==j[0] and abs(n.index(i[1])-n.index(j[1]))==1) or (i[1]==j[1] and abs(a.index(i[0])-a.index(j[0]))==1):
          ship.append(j)
      if len(ship)>1 and sorted(ship) not in cruisers:
        cruisers.append(sorted(ship))
    ret = 0
    for i in cruisers:
      if all([j in self.guesses for j in i]):
        ret+=1
    return ret
​
  def points(self):
    ret = len([i for i in self.guesses if i in self.scheme])
    ret+=2*self.sunk()
    return ret

