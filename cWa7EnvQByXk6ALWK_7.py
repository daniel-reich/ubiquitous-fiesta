
def golden_ratio():
  a,b=1,0
  for i in range(238): a,b=a+b,a
  return '1.'+str(int('1'+'0'*99)*b//a)

