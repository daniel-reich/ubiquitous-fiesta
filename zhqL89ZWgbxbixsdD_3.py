
def is_exact(n):
  m = int(n**(1/5)+2)
  res = [i for i in range(1,100) if fact(i) == n]
  return "Not exact!" if len(res) == 0 else [n,res[0]]
​
def fact(n): 
  return 1 if (n==1 or n==0) else n * fact(n - 1)

