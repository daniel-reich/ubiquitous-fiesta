
def rearranged_difference(num):
  y=str(num)
  o=''
  p=''
  z=[]
  for i in range(len(y)):
    if y[i].isdigit():
      z.append(int(y[i]))
  z.sort()
  for i in range(len(z)):
    o+=str(z[i])
  z.reverse()
  for i in range(len(z)):
    p+=str(z[i])
  return(int(p)-int(o))

