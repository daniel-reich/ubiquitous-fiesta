
def can_patch(bridge, planks):
  holes = []
  count = 0
  for i in bridge:
    if i == 1 and count != 0:
      holes.append(count)
      count = 0
    elif i == 0:
      count += 1
  for i in holes:
    repaired = False
    for j in planks:
      if i == j or i == j + 1:
        repaired = True
        planks.remove(j)
        break
    if not repaired and i != 1:
      return False
  return True

