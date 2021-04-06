
def is_repeated(strn):
  lg = len(strn)
  for i in range(1,len(strn)//2+1):
    if lg%i:
      continue
    tmp = strn[:i]
    lt = len(tmp)
    if tmp*(lg//lt) == strn:
      return lg//lt
  return False

