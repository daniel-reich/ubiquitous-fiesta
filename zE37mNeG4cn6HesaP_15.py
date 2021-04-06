
def max_ham(s1, s2):
  if s1 != s2 and sorted(s1) == sorted(s2):
    cnt = sum(a!=b for a,b in zip(s1,s2))
    return True if cnt == len(s1) else cnt
  return False

