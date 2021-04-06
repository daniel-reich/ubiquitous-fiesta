
def calculate_arrowhead(lst):
  lefty = 0
  righty = 0
  
  for i in lst:
    if(i[0] == '>'):
        righty+= len(i)
      
    elif(i[0] == '<'):
        lefty += len(i)
     
  motion = righty - lefty
  if(motion > 0):
      return '>'* motion
  
  elif(motion < 0):
      return '<'* abs(motion)
  
  else:
    return ''

