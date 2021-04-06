
def identify(*cube):
  i=0
  for c in cube:
    if len(cube)!=len(c):i+=1
  if len(cube[0])==4 and len(cube)==2:return 'Non-Full'
  return 'Missing {}'.format(i) if i!=0 else 'Full'

