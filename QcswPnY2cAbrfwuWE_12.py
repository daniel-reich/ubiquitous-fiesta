
def isfactoriel(n):
  mul=1
  for i in range(1,n+1):
    mul*=i
    if mul==n:
      return True
  return False
​
​
def filter_factorials(numbers):
  lst=[]
  for i in numbers:
    if isfactoriel(i):
      lst.append(i)
  return lst

