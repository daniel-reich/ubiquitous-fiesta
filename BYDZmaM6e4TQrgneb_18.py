
def fib_fast(num):
  fnMin1 = 1
  fnMin2 = 0
  fn = 1
  temp = 0
  if num == 0:
    return 0
  elif num == 1:
    return 1
  for i in range(2,num):
    #print (fnMin2, fnMin1, fn, i)
    temp = fn   
    fnMin2 = fnMin1
    fnMin1 = temp
    fn = fnMin1 + fnMin2
  return fn

