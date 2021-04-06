
def equal(a, b, c):
​
  count=0
  
  if(a==b and a==c and b==c):
    return 3
  elif(a==b or a==c or b==c):
    return 2
  else:
    return 0

