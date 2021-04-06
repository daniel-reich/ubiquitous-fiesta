
def empty_values(lst):
  result=[]
  for i in lst:
    result += [type(i)()]
  return result

