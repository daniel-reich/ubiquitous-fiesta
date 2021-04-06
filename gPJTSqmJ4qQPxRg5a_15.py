
def func(num):
  result=0
  for i in str(num):
    result+=int(i)
  return result-len(str(num))**2

