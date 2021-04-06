
def odds_vs_evens(num):
  b=str(num)
  a=len(b)
  sumOdd=0
  sumEven=0
  for i in range(0,a):
    c=int(b[i])
    if(c%2==0):
      sumEven=sumEven+c
    else:
      sumOdd=sumOdd+c
  if(sumEven>sumOdd):
    return "even"
  elif(sumOdd>sumEven):
    return "odd"
  else:
    return "equal"

