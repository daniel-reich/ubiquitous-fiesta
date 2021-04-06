
s=[1,2]
​
def ecg_seq_index(n):
  global s
  while not n in s:
    fx=set(factor(s[-1]));x=1;mem=s[-1];mcof=n**2
    while mem==s[-1]:
      mem2=set(i for i in fx if not x*i in s)
      mcof=min([x*i for i in mem2]+[mcof]);fx-=mem2
      if not fx or min(fx)*x>mcof:s+=[mcof]
      x+=1
  return s.index(n)
  
def factor(num):
  res=[];i=2
  while num!=1:
    while not num%i:
      res+=[i]
      num//=i
    i+=1
  return res

