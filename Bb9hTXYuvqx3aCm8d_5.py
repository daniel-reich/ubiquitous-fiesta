
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
​
  class Game:
​
    class Player:
​
      def __init__(self, string):
        self.str = list(string)
        self.points = 0
      
        self.indexes = {}
        self.removed = []
​
        for n in range(len(self.str)):
          self.indexes[n] = self.str[n]
​
      
      def remove(self, index):
        self.removed.append(index)
        ns = []
        for n in self.indexes.keys():
          if n not in self.removed:
            ns.append(self.indexes[n])
       # print(ns, self.removed, self.str, self.str == ns, index)
        self.str = ns
        return True
​
    def __init__(self, pA, pZ):
​
      self.rpA = pA
      self.rpZ = pZ
      
      self.pA = Game.Player(pA)
      self.pZ = Game.Player(pZ)
    
    def round(self, pAmove, pZmove):
      self.pA.remove(pZmove)
      self.pZ.remove(pAmove)
      #print(pAmove, pZmove, self.pA.str, self.pZ.str)
      return True
​
    def value(self):
      for n in range(len(self.pA.str)):
        pAl8r_val = ord(self.pA.str[n])
        pZl8r_val = ord(self.pZ.str[n])
        #print(pAl8r_val, pZl8r_val, self.pA.str[n], self.pZ.str[n])
        if pAl8r_val > pZl8r_val:
          self.pA.points += abs(pAl8r_val - pZl8r_val)
        elif pAl8r_val < pZl8r_val:
          self.pZ.points += abs(pAl8r_val - pZl8r_val)
        else:
          pass
          #return True
      return True
​
    def print(self):
      return {'A': self.pA.points, 'Z': self.pZ.points}
  
  game = Game(str_A, str_Z)
​
  for n in range(10):
    game.round(ind_A[n], ind_Z[n])
  
  game.value()
​
  return game.print()

