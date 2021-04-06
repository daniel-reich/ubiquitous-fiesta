
def factor_chain(lst):
  for i in range(1,len(lst)):
    if lst[i]%lst[i-1]==0:
      continue
    else:
      return False
  return True

