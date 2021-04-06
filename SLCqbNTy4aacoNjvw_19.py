
def remove_dups(lst):
  A=[]
  for x in lst:
    if x not in A:
      A.append(x)
  return A

