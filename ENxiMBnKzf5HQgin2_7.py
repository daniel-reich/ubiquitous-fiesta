
def pascal_row(n):
  
  print(n)
  x=[1]
  last=1
  for i in range(n):
    last=last*(n-i)//(i+1)
    x.append(last)
​
  return x

