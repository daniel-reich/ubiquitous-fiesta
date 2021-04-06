
def stock_picker(lst):
  a = max([lst[j]-lst[i] for i in range(len(lst)-1) for j in range(i+1,len(lst))])
  return a if a >0 else -1

