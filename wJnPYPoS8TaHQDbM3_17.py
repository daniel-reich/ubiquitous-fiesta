
def dice_roll(n, outcome):
  class Dice:
​
    def __init__(self, size = 6):
      self.size = size
      self.sides = list(range(1, size+1))
  
  def roll(dice, amount, previous = [], used = 0):
    if used == amount:
      return previous
    else:
      lsts = []
      if len(previous) == 0:
        for side in dice.sides:
          lsts.append([side])
      else:
        for lst in previous:
          for side in dice.sides:
            lsts.append(lst + [side])
      return roll(dice, amount, lsts, used + 1)
  
  d6 = Dice(6)
​
  r = roll(d6, n)
​
  return len([i for i in r if sum(i) == outcome])

