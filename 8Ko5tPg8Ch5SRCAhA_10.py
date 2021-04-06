
def fibonacci(num):
  a=[0,1]
  for x in range(0,num):
    a.append(a[x]+a[x+1])
  return a[-1]

