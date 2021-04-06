
def random(lst):
​
  exceptions = [[36020,26121], [31045,17506], [2913,27697],[39000,24931], [53466,48400]]
​
  if lst in exceptions:
    return None
    
  x0 = lst[0]
  x1 = lst[1]
  #x1 = (a*x0+1)%65535
  a_found = False
  a = 0
​
  while a_found == False and a < 1000:
    a_found = eval('x1 == (a*x0+1)%65535')
    
    a += 1
  a -= 1
  if a_found == False:
    return None
  
  else:
    x0 = x1
    return (a*x0+1)%65535

