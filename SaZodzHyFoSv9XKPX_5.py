
class Domino_Game:
  class Domino:
​
    def __init__(self, pos, is_dom):
​
      self.p = pos
​
      self.id = is_dom != ' '
      self.du = is_dom == '|'
​
      self.next = pos + 1
    
    def can_flip(self):
      return self.id == self.du == True
    
    def flip(self):
      self.du = False
      return True
    
    def __str__(self):
      if self.id == False:
        return ' '
      else:
        if self.du == False:
          return '/'
        else:
          return '|'
  
  def __init__(self, domino_string):
    self.ds = domino_string
​
    self.dominos = {n: Domino_Game.Domino(n, domino_string[n]) for n in range(len(domino_string))}
  
  def play(self):
    for n in sorted(self.dominos.keys()):
      domino = self.dominos[n]
      if domino.can_flip() == False:
        break
      else:
        domino.flip()
    return True
  
  def __str__(self):
    tr = ''
    for n in sorted(self.dominos.keys()):
      domino = self.dominos[n]
      tr += str(domino)
    return tr
  
​
def domino_chain(dominos):
​
  dg = Domino_Game(dominos)
​
  dg.play()
​
  return str(dg)

