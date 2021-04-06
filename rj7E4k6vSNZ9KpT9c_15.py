
def factor_chain(lst):
  for idx, number in enumerate(lst[1:]):
    if number%lst[idx] != 0:
      return False
  return True

