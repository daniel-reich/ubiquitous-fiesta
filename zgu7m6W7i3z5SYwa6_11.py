
def is_equal(lst):
  value1 = str(lst[0])
  value2 = str(lst[1])
  returnvalue1 = 0
  returnvalue2 = 0 
  
  for x in value1:
    returnvalue1 += int(x)
  
  for y in value2:
    returnvalue2 += int(x)
  
  if returnvalue1 == returnvalue2:
    return True 
  return False

