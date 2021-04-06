
def maya_number(n):
  x=[]
  while n: x=[n%20]+x; n//=20
  return [["@"],[["@",i%5*"o"+i//5*"-"][bool(i)] for i in x]][bool(x)]

