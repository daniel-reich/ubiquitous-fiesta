
def parse_list(lst):
  A=[]
  for x in lst:
    if type(x)==int:
      A.append(str(x))
    else:
      A.append(x)
  return A

