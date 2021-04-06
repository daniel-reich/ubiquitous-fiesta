
def amount_fib(n):
  a,lst = 2,[]
  if n ==1: lst = [0]
  elif n > 1: lst = [0,1,1]
  while a < n:
    lst.append(a)
    a = lst[len(lst) - 2] + lst[len(lst) - 1]
  return len(lst)

