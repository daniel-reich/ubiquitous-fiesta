
def can_patch(bridge, planks):
  holes = []
  hole = 0
  for i, x in enumerate(bridge):
    if i > 0 and x == 0:
      if bridge[i - 1] == 1:
        start = i
      hole += 1
    if i < len(bridge)-1 and x == 0 and bridge[i+1] == 1:
      holes.append(hole)
      hole = 0
​
  holes = list(filter(lambda a: a != 1, holes)) # remove holes of length 1
​
  if len(holes) > len(planks):
    return False
​
​
  for i in range(len(holes)):
    if holes.pop(holes.index(max(holes))) > planks.pop(planks.index(max(planks)))+1:
      return False
​
  return True

