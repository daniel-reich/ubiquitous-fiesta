
def every_some(test, val, a, b, c, d, e, f = None, g = None):
  to_test = [a, b, c, d, e]
  
  if f != None:
    to_test.append(f)
  if g != None:
    to_test.append(g)
  
  count = 0
  
  for item in to_test:
    if eval('{}{}'.format(item, test)) == True:
      count += 1
  
  if val == 'everybody':
    return count == len(to_test)
  elif  val == 'somebody':
    return count >= 1
  else:
    return 'Incorrect Value: {}'.format(val)

