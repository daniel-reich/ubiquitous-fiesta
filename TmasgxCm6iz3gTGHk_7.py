
def min_length(lst, n):
  cl = 1  
  while not any([ sum(lst[i:i+cl]) > n for i in range(len(lst)-cl+1)]):
    if cl < len(lst):
      cl += 1
    else:
      return -1
  return cl

