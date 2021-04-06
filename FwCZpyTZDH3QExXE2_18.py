
def amount_fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  arr = [0,1]
  while arr[-1] < n:
    arr.append(arr[-1] + arr[-2])
  return len(arr)-1

