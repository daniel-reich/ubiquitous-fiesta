
def is_polydivisible(n):
  if n<10:return True
  else:
    for i in range(2,len(str(n))+1):
      if (int(str(n)[:i])/i)%1:return False
  return True

