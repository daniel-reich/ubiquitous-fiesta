
def max_ham(s1, s2):
  if sorted(s1) == sorted(s2):
    distance = sum(x!=y for (x,y) in zip(s1,s2))
    if distance < len(s1):
      return distance
    return distance == len(s1)
  return False

