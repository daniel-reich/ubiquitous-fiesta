
def loneliest_number(lo, hi):
  dis = 0
  for n in range(lo, hi+1):
    d = 1
    while not (isprime(n+d) or isprime(n-d)): d+=1
    if d>dis:
      num = n
      dis = d
      clo = n+d if isprime(n+d) else n-d
  return {'number':num, 'distance':dis, 'closest':clo}
​
isprime = lambda n: n>1 and all(n%i for i in range(2,1+int(n**.5)))

