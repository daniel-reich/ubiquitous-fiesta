
def crop_hydrated(field):
  length=len(field)
  width=len(field[0])
  flag=True
  
  def check(x, i):
    try:
      if(field[x+1][i]=="w"):
        print('test1')
        return True
    except:
      pass
      
    try:
      if(field[x-1][i]=="w" and (x-1)>=0):
        print('test2')
        return True
    except:
      pass
      
    try:
      if(field[x][i+1]=="w"):
        print('test3')
        return True
    except:
      pass
      
    try:
      if(field[x][i-1]=="w" and (i-1)>=0):
        print('test4')
        return True
    except:
      pass
      
    try:
      if(field[x+1][i+1]=="w"):
        print('test5')
        return True
    except:
      pass
      
    try:
      if(field[x-1][i-1]=="w" and (x-1)>=0 and (i-1)>=0):
        print('test6')
        return True
    except:
      pass
      
    try:
      if(field[x+1][i-1]=="w" and (i-1)>=0):
        print('test7')
        return True
    except:
      pass
      
    try:
      if(field[x-1][i+1]=="w" and (x-1)>=0):
        print('test8')
        return True
    except:
      pass
      
  for x in range(len(field)):
    for i in range(len(field[x])):
      if(field[x][i]=="c"):
        if(check(x, i)):
          continue
        else:
          print('error')
          flag=False
  return flag

