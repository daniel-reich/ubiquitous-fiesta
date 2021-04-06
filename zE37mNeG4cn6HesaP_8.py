
def max_ham(s1, s2):
  if sorted(s1) != sorted(s2): return False
  c=0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      c+=1
  return True if c==len(s1) else c

