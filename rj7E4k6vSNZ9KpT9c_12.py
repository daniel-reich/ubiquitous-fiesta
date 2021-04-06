
def factor_chain(lst):
  for i in range(len(lst)):
    if i == len(lst)-1:
      break
    if lst[i+1] % lst[i] !=0:
      return False
  return True

