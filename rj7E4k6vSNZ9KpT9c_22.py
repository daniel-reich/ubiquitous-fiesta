
def factor_chain(lst):
  return False not in [lst[i] % lst[i-1] == 0 for i in range(1, len(lst))]

