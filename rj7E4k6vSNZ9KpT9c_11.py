
def factor_chain(lst):
  for i in range(len(lst)-1, -1, -1):
    if (lst[i]) % lst[i-1] != 0:
      return False
    else:
      return True

