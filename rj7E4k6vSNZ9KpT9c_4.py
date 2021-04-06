
def factor_chain(lst):
  return all(i % lst[idx-1] == 0 for idx, i in enumerate(lst[1:], 1))

