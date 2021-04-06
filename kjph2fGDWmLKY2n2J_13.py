
def valid_color (color):
  
  c=color.split('(')
  c=c[1].split(')')
  c=c[0]
  c=c.split(',')
  if('a' in color and len(c)!=4):
    return False
  if(len(c)==4 and 'a' not in color):
    return False
  if(color[3]==' '):
    return False
  for i in range(len(c)):
    if("%" in c[i]):
      m=eval(c[i][:-1])
      if(m>100):
        return False
    elif(len(c[i])==0):
      return False
    else:
      m=eval(c[i])
    if(m<256 and m>=0 and i<3):
      a=1
    elif(i==3 and m>=0 and m<=1):
      a=1
    else:
      return False
  return True

