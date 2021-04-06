
def swap_cards(n1, n2):
  s1 = str(n1)
  s2 = str(n2)
  if min(s1[0],s1[1]) == s1[0] or s1[0]==s1[1]:
    n1 = int(s2[0]+s1[1])
    n2 = int(s1[0]+s2[1])
  else:
    n1 = int(s1[0]+s2[0])
    n2 = int(s1[1]+s2[1])
  return n1>n2

