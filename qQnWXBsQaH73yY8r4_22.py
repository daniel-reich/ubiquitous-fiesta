
def dFact(N):
    arr={}
    if N in arr:
        return arr[N]
    elif N == 0 or N == 1:
        return 1
        arr[N] = 1
    else:
        factorial = N*dFact(N - 1)
        arr[N] = factorial
    return factorial
​
def kempner(n):
  if n == 1:
    return 1
  for i in range(n+1):
    if dFact(i)%n == 0:
      return i

