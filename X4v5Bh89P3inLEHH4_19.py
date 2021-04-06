
def spin_around(x):
  rot = 0
  for i in x:
    if i == 'right':
      rot += .25
    else:
      rot -= .25
​
  return abs(rot) if rot % 1 == 0 else 0

