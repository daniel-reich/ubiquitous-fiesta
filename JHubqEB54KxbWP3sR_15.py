
def dist(line,x,y):
  l1=line.replace('x','*'+str(x))
  l2=l1.replace('y=','')
  l3=line.split('=')
  a=eval(l3[1].split('x')[0])
  return round(abs(eval(l2)-y)/(a**2+1)**0.5,2)

