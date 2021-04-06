
class Person:
  def __init__(self,n,l_like,l_hate):
    self.n=n
    self.l_like=l_like
    self.l_hate=l_hate
    
  def taste(self,i):
    return "{} eats the {}{}!".format(self.n,i," and loves it" if i in self.l_like else " and hates it" if i in self.l_hate else "")

