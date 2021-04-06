
def fib_str(n, lst):
  while len(lst) < n:
    lst.append(lst[-1]+lst[-2])
  return ', '.join(lst)

