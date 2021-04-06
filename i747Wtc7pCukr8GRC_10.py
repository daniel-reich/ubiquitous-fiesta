
def max_product(lst):
  if len(lst) == 3:
    return lst[0]*lst[1]*lst[2]
  pos = [el for el in lst if el>=0]
  neg = [el for el in lst if el < 0]
  pos.sort()
  neg.sort()
  p1 = -500
  p2 = -500
  if len(pos) == 0:
    p2 = neg[-1]*neg[-2]*neg[-3]
    return p2
  if len(pos) >= 3:
    p1 = pos[-1]*pos[-2]*pos[-3]
  if len(neg) >= 2:
    p2 = neg[0]*neg[1]*pos[-1]
  if p1 >= p2:
    return p1
  else:
    return p2
​
def min_product(lst):
  if len(lst) == 3:
    return lst[0]*lst[1]*lst[2]
  pos = [el for el in lst if el>=0]
  neg = [el for el in lst if el < 0]
  pos.sort()
  neg.sort()
  p1 = 1000
  p2 = 1000
  if len(neg) == 0:
    p2 = pos[-1]*pos[-2]*pos[-3]
    return p2
  if len(neg) >= 3:
    p1 = neg[0]*neg[1]*neg[2]
  if len(pos) >= 2:
    p2 = pos[-1]*pos[-2]*neg[0]
  if p1 <= p2:
    return p1
  else:
    return p2

