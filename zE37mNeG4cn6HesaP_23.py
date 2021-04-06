
def max_ham(s1, s2):
  if not(all(i in s2 for i in s1)and all(i in s1 for i in s2)):return False
  a = sum([s1[i]!=s2[i] for i in range(len(s1))])
  return True if a==len(s1) else a

