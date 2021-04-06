
def max_ham(s1, s2):
  if sorted(list(s1)) != sorted(list(s2)):
    return False
  
  d = sum(1 for i in range(len(s1)) if s1[i] != s2[i])
  return d if d != len(s1) else True

