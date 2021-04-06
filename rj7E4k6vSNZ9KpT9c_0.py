
def factor_chain(lst):
  for x in lst:
    if (lst[-1]%x != 0):
      return False
  return True

