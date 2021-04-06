
def postfix(expression):
  ex = expression.replace('/','//').split()
  ind = 0
  while len(ex)>1 and ind<len(ex):
    if ex[ind] in '+-*//':
      temp = eval(ex[ind-2]+ex[ind]+ex[ind-1])
      ex = ex[:ind-2]+[str(temp)]+ex[ind+1:]
      ind = 0
    else:
      ind+=1
  return int(ex[0])

