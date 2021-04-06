
def boom_intensity(n):
  if n<2:
    return 'boom'
  b = 'B{}m'.format('o'*n)
  if n%2==0 and n%5==0:
    return b.upper() + '!' 
  elif n%2==0:
    return b +'!' 
  elif n%5==0:
    return b.upper() 
  return b

