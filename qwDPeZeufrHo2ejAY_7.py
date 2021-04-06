
def eval_algebra(eq):
  list1 = eq.split()
  result = []
  
  for item in list1:
    try:
      result.append(int(item))
    except:
      result.append(item)
      
  if result[4] == 'x':
    if result[1] == '+':
      return result[0] + result[2]
    return result[0] - result[2]
  elif result[0] == 'x':
    if result[1] == '+':
      return result[4] - result[2]
    return result[4] + result[2]
  elif result[1] == '+':
    return result[4] - result[0]
  return (result[4] - result[0]) * -1

