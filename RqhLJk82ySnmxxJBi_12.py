
def power_morphic(num):
  l=[2,3,4,5,6,7,8,9,10]
  c=0
  for i in l:
    if(str(num**i).endswith(str(num))):
      c+=1
  if(c==9):
    return "Polymorphic"
  elif(c==4):
    return "Quadrimorphic"
  elif(c==2):
    return "Dimorphic"
  elif(c==1):
    return "Enamorphic"
  else:
    return "Amorphic"

