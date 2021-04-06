
def amount_fib(n):
  lst = [0,1]
  while lst[-1]<n:
    lst.append(lst[-1]+lst[-2])
  return len([i for i in lst if i<n])

