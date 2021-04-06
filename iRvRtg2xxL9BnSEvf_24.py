
class Person:
  def __init__(self, name, like, dislike):
    self.name=name
    self.like=like
    self.dislike=dislike
  def taste(self, item):
    l= ''
    if item in self.like: l=' and loves it' 
    if item in self.dislike: l= ' and hates it'
    
    return '{} eats the {}{}!'.format(self.name,item,l)

