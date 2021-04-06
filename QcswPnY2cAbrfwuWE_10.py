
import itertools
​
def calcFactorial(n, tbl):
  print('n=',n)
  if len(tbl)<n: tbl+=[None]*(2*n-len(tbl))
  if tbl[n]: return tbl[n]  
  if n==0 or n==1: res=1
  else: 
    print('calc')
    res=n*calcFactorial(n-1, tbl)
  tbl[n]=res
  return res
  
def filter_factorials(numbers):
  factResTable=[None]*100
  res=[]
  j=0
  for i in itertools.count(1):
    x=calcFactorial(i, factResTable)
    if x<numbers[j]: continue
    while x>=numbers[j]:
      if x==numbers[j]: res.append(x)
      j+=1
      print('j=',j)
      if j==len(numbers): return res

