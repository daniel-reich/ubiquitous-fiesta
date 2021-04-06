
def straight_digital(n):
  if n<100:
    return "Not Straight"
  n = str(n)
  l=[]
  for i in range(1, len(n)):
    l.append(int(n[i])-int(n[i-1]))
  if set(l)=={0}:
    return "Trivial Straight"
  elif len(set(l))==1:
    return int(n[i])-int(n[i-1])
  return "Not Straight"

