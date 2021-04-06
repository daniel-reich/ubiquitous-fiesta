
def letter_distance(t1, t2):
  sm = min(len(t1), len(t2))
  d=0
  for i in range(sm):
    d+= abs(ord(t1[i])-ord(t2[i]))
  return d + abs(len(t1)-len(t2))

