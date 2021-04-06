
def fibonacci(n):
  lst = [0,1]
  while len(lst)<=n:
    lst.append(lst[-1]+lst[-2])
  return str(lst[n])

