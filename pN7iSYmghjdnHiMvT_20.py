
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
    self.__hits = 0
    self.__points = 0
    self.__sunk = 0
    self.cnt = 0
    # create board
    self.bd = [[' ' for i in range(5)] for j in range(5)]
    # load board with ships
    for item in scheme:
      self.bd[ord(item[0]) - 65][int(item[1]) - 1] = 's'
    # load guesses
    for item in self.guesses:
      if self.bd[ord(item[0]) - 65][int(item[1]) - 1] == 's':
        self.bd[ord(item[0]) - 65][int(item[1]) - 1] = 'X'
        self.__hits += 1
        self.__points += 1
      else:
        self.bd[ord(item[0]) - 65][int(item[1]) - 1] = '.'
    # count sunk crusiers
    for i in range(len(self.bd)):
      for j in range(len(self.bd[i])):
        if self.bd[i][j] == 'X' and self.sunk_crusiers(i, j):
          self.cnt += 1
    self.__sunk = self.cnt // 2
    self.__points += self.cnt
  
  def sunk_crusiers(self, pi, ci):
    if pi > 0 and self.bd[pi - 1][ci] == 'X':
      return True
    elif pi < 4 and self.bd[pi + 1][ci] == 'X':
      return True
    elif ci > 0 and self.bd[pi][ci - 1] == 'X':
      return True
    elif ci < 4 and self.bd[pi][ci + 1] == 'X':
      return True
    else:
      return False
      
  def board(self):
    return self.bd
      
  def hits(self):
    return self.__hits
​
  def sunk(self):
    return self.__sunk
​
  def points(self):
    return self.__points

