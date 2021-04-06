
def boolean_and(lst):
  result = True
  for element in lst:
    result = result and element
  return result
​
def boolean_or(lst):
  result = False
  for element in lst:
    result = result or element
  return result
  
def boolean_xor(lst):
  result = lst[0]
  for element in lst[1:]:
    if result == element:
      result = False
    else:
      result = True
  return result

