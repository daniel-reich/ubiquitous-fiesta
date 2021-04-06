
def split_bunches(bunches):
  A=[]
  for x in bunches:
    A+=[x]*x['quantity']
  for x in A:
    x['quantity']=1
  return A

