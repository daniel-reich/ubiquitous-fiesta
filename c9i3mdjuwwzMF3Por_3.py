
def bemirp(n):
  d={'0':'0','1':'1','6':'9','8':'8','9':'6'}
  fn=int(str(n)[::-1])
  res=0
  if prime(n):
    res+=1
    if n!=fn and prime(fn):
      res+=1
      res+=all(i in d for i in str(n)) and\
        all(prime(int(''.join(d[i] for i in str(num)))) for num in [n,fn])
  return ['C','P','E','B'][res]
​
def prime(num):
    return num>1 and all(num%i for i in range(2,num//2+1))

