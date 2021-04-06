
def factor_chain(lst):
  for counter in range(len(lst) - 1):
    if lst[counter+1] % lst[counter] != 0:
      return False
      
  return True

