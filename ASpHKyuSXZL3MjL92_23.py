
def amplify(num):
  y = []
  for x in range(1, num+1):
    if x%4 == 0:
      y.append(x*10)
    else:
      y.append(x)
  return(y)

