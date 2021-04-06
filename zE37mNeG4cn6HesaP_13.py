
def max_ham(s1, s2):
  r=[i==h for i,h in zip(s1,s2)].count(True)
  return False if sorted(s1)!=sorted(s2) else True if r==0 else len(s1)-r

