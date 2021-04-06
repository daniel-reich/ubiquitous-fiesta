
def stmid(string):
  
  x=string.split(' ')
  new=[]
  for i in x:
    if len(i) %2==0:
      new.append(i[0])
    else:
      new.append(i[len(i)//2])
  return ''.join(new)

