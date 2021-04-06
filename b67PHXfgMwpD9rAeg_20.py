
def plus_sign(txt): 
  for x in range(1,len(txt))[:-1]:
    if txt[x].isalpha() and (txt[x-1]!='+' or txt[x+1]!='+'):
      return False
  return False if txt[0].isalpha() else True

