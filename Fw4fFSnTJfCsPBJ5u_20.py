
def how_many_missing(lst):
  
  list_length = len(lst)
​
  '''ordered number line'''
  num_line = []
  
  '''bulding the line'''
  if list_length == 1:  
    num_line.append(lst[0])
  elif list_length == 0:  pass
  else:
    for i in range(lst[0], lst[-1]):
      num_line.append(i)
    num_line.append(lst[-1])
    
  return len(num_line) - list_length

