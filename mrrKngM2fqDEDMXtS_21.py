
def can_patch(bridge, planks):
  holes = []
  amount = 0
  for i in bridge:
    if i == 0:
      amount += 1
    elif not amount == 0:
      holes.append(amount)
      amount = 0
  
  for hole in holes:
    if hole - 1 in planks:
      planks.remove(hole - 1)
    elif hole in planks:
      planks.remove(hole)
    elif hole > 1:
      return False
  
  return True

