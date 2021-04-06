
def ss(num):
  f=True
  if num==1 or num==0:
    f=False
  else:
    for i in range(2,num):
      if num%i==0:
        f=False
  return f
def extract_primes(num):
  m=[]
  s=str(num)
  for i in range(len(s)):
    if s[i]!='0':
      for j in range(i+1,len(s)+1):
        a=int(s[i:j])
        if ss(a):
          m.append(a)
  m.sort()
  return m

