
def min_swaps(string):
  l0,l1=("01"*((len(string)//2)+1))[:-1],("10"*((len(string)//2)+1))[:-1]
  return min(len([1 for i,h in zip(string,l0) if i==h]),len([1 for i,h in zip(string,l1) if i==h]))

