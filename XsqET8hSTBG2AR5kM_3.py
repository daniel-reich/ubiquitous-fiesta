
def letter_distance(t1, t2):
  l1,l2 = len(t1),len(t2)
  return sum(abs(ord(t1[i])-ord(t2[i])) for i in range(min(l1,l2))) + abs(l1-l2)

