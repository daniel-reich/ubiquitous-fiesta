
def integer_boolean(n):
  list = []
  
  for i in n:
    if i == '1':
      list.append(True)
      
    elif i == '0':
      list.append(False)
    
  return list

