
# Check the Resources tab for the list of characters and items.
class cClass():
  name = 'error'
  attack = 0
  defense = 0
  speed = 0
​
  def __init__(self, name):
    self.name = name
    if name == 'Knight':
      self.attack = 120
      self.defense = 140
      self.speed = 6
    elif name == 'Warrior':
      self.attack = 180
      self.defense = 71
      self.speed = 8
    elif name == 'Fairy':
      self.attack = 71
      self.defense = 100
      self.speed = 16
    elif name == 'Robot':
      self.attack = 160
      self.defense = 120
      self.speed = 11
    elif name == 'Giant':
      self.attack = 160
      self.defense = 200
      self.speed = 4
​
def max_stats(character, gold):
  you = cClass(character)
  
  if gold >= 100:
    mAttack = 50
  else:
    mAttack = int(gold / 20) * 10
  
  if gold >= 150:
    mDefense = 100
  else:
    mDefense = int(gold / 30) * 20
  
  if gold >= 120:
    mSpeed = 15
  else:
    mSpeed = int(gold / 24) * 3
  
  return [mAttack + you.attack, mDefense + you.defense, mSpeed + you.speed]

