
def max_ham(s1, s2):
  chk1,chk2 = sorted(s1), sorted(s2)
  if chk1 != chk2:
    return(False)
  retno = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      retno += 1
  if retno == len(s1):
    return(True)
  else:
    return(retno)

