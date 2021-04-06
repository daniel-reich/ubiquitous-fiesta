
def divid(x, y,count):
  # Your recursive solution here.
  if abs(x)<abs(y):
    if x*y>=0:
      return count
    else:
      return -count
  elif x*y>0:
    x=x-y
    count=count+1
    return divid(x,y,count)
  elif x*y<0:
    x=x+y
    count=count+1
    return divid(x,y,count)
def divide(x,y):
  return divid(x,y,0)

