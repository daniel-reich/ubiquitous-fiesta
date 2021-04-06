
def fib_fast(n):
  lst = [0,1]
  for i in range(2, n+1):
    lst.append(lst[i-2] + lst[i-1])
  return lst[n]

