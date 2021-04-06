
def complete_square(lst):
  r,c=len(lst),len(lst[0])
  if r==c:
    return lst
  elif r>c:
    return [x+[0]*(r-c) for x in lst]
  else:
    return lst+[[0]*c]*(c-r)

