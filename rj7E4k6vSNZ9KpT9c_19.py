
def factor_chain(lst):
  return not sum( [ 1 for i in range(len(lst)-1) if lst[i+1] % lst[i] ] )

