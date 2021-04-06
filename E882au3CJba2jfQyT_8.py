
def common_elements(lst1, lst2):
  A=[]
  for x in lst1:
    if x not in A and x in lst2:
      A.append(x)
  return A

