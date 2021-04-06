
def id_mtrx(n):
  if type(n)!=int:
    return 'Error' 
  else:
    lst= [[1 if x==y else 0 for y in range(abs(n))]for x in range(abs(n))]
    return lst if n>0 else lst[::-1]

