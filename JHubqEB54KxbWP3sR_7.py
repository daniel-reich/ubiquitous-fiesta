
def dist(s, a, b):
  n = s.split('=')[1].find('x')
  i,j = s.split('=')[1][:n],1
  s1 = s.split('=')[1].replace('x','*'+str(a))+'-'+str(b)
  res =(eval(s1)/((eval(i)**2)+1)**0.5)
  return abs(round(res,2))

