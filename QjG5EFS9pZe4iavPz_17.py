
def fib(n):
  arr = [0,1]
  for i in range(n):
    arr.append(arr[-1] + arr[-2])
  return arr[n]

