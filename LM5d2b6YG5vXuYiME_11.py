
def can_enter_cave(x):
  x.append("Blank for Reasons I can't comprehend.")
  setx = ""
  sety = ""
  row0 = x[0]
  row1 = x[1]
  row2 = x[2]
  row3 = x[3]
  row4 = x[4]
  print(row0)
  print(row1)
  print(row2)
  print(row3)
  print(row4)
  count = 0
  
  
  for j in range(7):
    count = 0
    if j < 1:
      pass
    else:
      sety = setx
      setx = ""
    for i in range(5):
      if get(i,j,row0,row1,row2,row3,row4) == 0:
        setx = setx + "0"
      else:
        setx = setx + "1"
    if j > 0:
      for i in range(5):
        if setx[i] == "0":
          if sety[i] == "0":
            count += 1
      if count == 0:
        print("False")
        return False
    else:
      pass
  print("True")
  return True
  
def get(x,y,row0,row1,row2,row3,row4):
  if  x == 0:
    return row0[y]
  if  x == 1:
    return row1[y]
  if  x == 2:
    return row2[y]
  if  x == 3:
    return row3[y]
  if  x == 4:
    return row4[y]
  if  x == 5:
    return row5[y]
  if  x == 6:
    return row6[y]
  if  x == 7:
    return row7[y]
    
def chkxl(x):
  if x == 0:
    return False
  else:
    return True
def chkxu(x):
  if x == 3:
    return False
  else:
    return True
def chkyl(y):
  if y == 0:
    return False
  else:
    return True
def chkyu(y):
  if y == 7:
    return False
  else:
    return True

