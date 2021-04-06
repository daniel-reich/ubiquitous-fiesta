
def can_patch(bridge, planks):
  b = ''.join(str(i) for i in bridge)
  holes = [len(i) for i in b.split('1')]
  if all(i<=1 for i in holes):
      return True
  elif all(planks.count(i-1) + planks.count(i)>=holes.count(i) for i in holes if i>1):
      return True
  return False

