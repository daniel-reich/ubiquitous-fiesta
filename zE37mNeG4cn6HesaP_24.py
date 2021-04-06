
def max_ham(s1, s2):
  if set(s1) != set(s2):
    return False
  distance = sum([1 for i in range(len(s1)) if s1[i] != s2[i]])
  if distance == len(s1):
    return True
  else:
    return distance

