
def factor_chain(lst):
  for i in range(0, len(lst) - 1):
    if lst[i + 1] % lst[i] != 0:
      return False
  return True

