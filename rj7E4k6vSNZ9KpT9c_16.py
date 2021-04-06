
def factor_chain(lst):
  return all([lst[x] % lst[x -1] == 0 for x in range(1, len(lst))])

