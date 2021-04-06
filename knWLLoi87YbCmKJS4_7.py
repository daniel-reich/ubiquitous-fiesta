
def happy(n):
  for i in range(10):
    numbers = []
    while n>0:
      numbers.append(n%10)
      n = int(n/10)
    numbers = list(map(lambda x:x*x,numbers))
    n = sum(numbers)
  if n==1:
    return True
  else:
    return False

