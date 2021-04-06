
def valid_color (color):
  result = True
  if color[3] == 'a':
    rgba_flag = 1
    valuestxt = color[5:-1]
  elif color[3] == '(':
    rgba_flag = 0
    valuestxt = color[4:-1]
  else:
    result = False
    return result
    
  print(valuestxt)
  valuelst = valuestxt.split(',')
  if '' in valuelst:
    result = False
    return result
  if rgba_flag == 1 :
    if len(valuelst) != 4:
      result = False
      return result
  if rgba_flag == 0 :
    if len(valuelst) != 3:
      result = False
      return result 
  
  if '%' in valuelst[0]:
    percentage_flag = 1
    for i in range(len(valuelst)):
      if int(valuelst[i][:-1]) < 0 or int(valuelst[i][:-1]) > 100:
        result = False
    return result
  else:
    percentage_flag = 0
    for i in range(3):
      if int(valuelst[i]) < 0 or int(valuelst[i]) > 255:
        result = False
    if rgba_flag == 1:
      if float(valuelst[3]) < 0 or float(valuelst[3]) > 1:
        result = False
    return result
    
  return result

