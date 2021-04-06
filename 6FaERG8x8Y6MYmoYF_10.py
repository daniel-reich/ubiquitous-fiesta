
def dice_score(throw):
  sum = 0
  x = throw.count(1)
  if x >= 3:
    sum = sum + 1000 +(x-3)*100
  else:
    sum = sum + x * 100
  y = throw.count(2)
  if y >= 3:
    sum = sum + 200 
  z = throw.count(3)
  if z >= 3:
    sum = sum + 300
  m = throw.count(4)
  if m >= 3:
    sum = sum + 400
  n = throw.count(5)
  if n >= 3:
    sum = sum + 500 +(n-3)*50
  else:
    sum = sum + n *50
  o = throw.count(6)
  if o >= 3:
    sum = sum + 600
   
  return sum

