
def factor_chain(lst):
  return len([x for x in range(len(lst)-1) if lst[x+1] % lst[x] == 0]) > 1

