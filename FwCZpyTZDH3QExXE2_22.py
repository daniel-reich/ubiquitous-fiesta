
def amount_fib(n):
  lst = [0,1]
  if n < 2:
    return n
  while n > lst[-1]:
    lst.append(lst[-1] + lst[-2])
  return len(lst) - 1

