
def divide(x, y,counter = 0,negative = False):
  if counter == 0:negative,x,y = [False,True,False][(x>0)+(y>0)],abs(x),abs(y)
  if x>=y:return divide(x-y,y,counter+1,negative)
  else:return int(counter)*[1,-1][negative]

