
def pairs(lst):
  return [[lst[i],lst[-i-1]] for i in range(len(lst)) if 2*i+1<=len(lst)]

