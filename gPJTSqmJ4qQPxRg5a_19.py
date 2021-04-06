
def func(num):
  n=str(num)
  s=0
  for i in n:
    s+=int(i)
  return s-(len(n)**2)

