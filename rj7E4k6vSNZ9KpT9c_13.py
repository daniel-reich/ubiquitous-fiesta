
def factor_chain(lst):
  return all([True if(lst[i]%lst[i-1]==0) else False for i in range(1, len(lst))])

