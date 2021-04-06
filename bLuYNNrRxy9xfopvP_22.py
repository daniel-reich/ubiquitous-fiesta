
def yahtzee_score_calc(lst):
  
  class Game:
​
    def __init__(self, points = 0, round_num = 1, bonus = False):
      self.p = points
      self.r = round_num
      self.b = bonus
    
    def rond(self, lst):
      
      r = self.r
​
      if r in range(1, 6):
        tr = lst.count(r) * r
      elif r == 6:
        tr = lst.count(r) * r
        if self.p + tr >= 63:
          self.b = True
      elif r == 7:
        tr = 0
        for item in lst:
          c = lst.count(item)
          if c >= 3:
            tr = sum(lst)
            break
      elif r == 8:
        
        if lst.count(lst[0]) >= 4 or lst.count(lst[1]) >= 4:
          tr = sum(lst)
        else:
          tr = 0
      elif r == 9:
        s = list(set(lst))
​
        if len(s) == 2:
          c1 = lst.count(s[0])
          c2 = lst.count(s[1])
​
          if (c1 == 2 and c2 == 3) or (c2 == 2 and c1 == 3):
            tr = 25
          else:
            tr = 0
        else:
          tr = 0
      elif r == 10:
        seqs = ['1234', '2345', '3456', '4567', '5678', '6789']
​
        ls = ''
        for item in sorted(lst):
          ls += str(item)
        
        tr = 0
        for seq in seqs:
          if seq in ls:
            tr = 30
            break
      elif r == 11:
        seqs = ['12345', '23456', '34567', '45678', '56789']
​
        ls = ''
        for item in sorted(lst):
          ls += str(item)
        
        tr = 0
        for seq in seqs:
          if seq in ls:
            tr = 40
            break
      elif r == 12:
        if lst.count(lst[0]) == 5:
          tr = 50
        else:
          tr = 0
      elif r == 13:
        tr = sum(lst)
      
      self.p += tr
      self.r += 1
      
      return True
​
    def add_bonus(self):
      if self.b == True:
        self.p += 35
      return True
    
​
  g1 = Game()
​
  for l in lst:
    r = g1.rond(l)
​
  g1.add_bonus()
​
  return g1.p

