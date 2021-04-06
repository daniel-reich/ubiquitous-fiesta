
def greaterThanOne(frac):
  x = frac.split('/')
  if int(x[0])/int(x[1]) > 1:
    return True
  else: 
    return False

