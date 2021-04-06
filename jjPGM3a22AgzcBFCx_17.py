
def decrypt(lst):
  lookuplist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  
  for i in range(1,27):
    if i in lst:
      pass
    else:
      return lookuplist[i-1]

