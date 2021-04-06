
def factor_chain(lst):
  for x in range (1,len(lst)):
    if lst[x]%lst[x-1]!=0:
      return False
  return True

