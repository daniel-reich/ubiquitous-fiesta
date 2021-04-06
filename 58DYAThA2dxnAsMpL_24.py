
def integer_boolean(n):
  new_list = [] 
  for i in range(len(n)): 
    if n[i] == '1':
      new_list.append(True)
    else:
      new_list.append(False)
  return new_list

