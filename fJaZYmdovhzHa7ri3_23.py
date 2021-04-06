
def max_collatz(num):
  M = num
  while num!=1:
    num=iter(num)
    M=max(M,num)
  return M
​
iter = lambda n: 3*n+1 if n%2 else n//2

