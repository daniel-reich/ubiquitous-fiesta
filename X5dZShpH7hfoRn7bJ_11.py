
from itertools import combinations_with_replacement
def prime_set (n):
  prime=[]
  for i in range (2,n+1):
    counter=0
    for j in range (1,i+1):
      if i%j ==0:
        counter+=1
    if counter <=2:
      prime.append(i)
  return prime
​
def c_fuge(n, k):
  if k==1 or k==0:
    return False
  if k==n:
    return True
  lst1,all_,sumsum=prime_set(n),[],[]
  lst = [i for i in lst1 if n%i==0]
  if n in lst:
    return False
  for j in range (1,n//2):
    all_.append(list(combinations_with_replacement(lst,j)))
  
  sumsum=[sum(j) for i in all_ for j in i]
  if k in sumsum and (n-k) in sumsum:
    return True
  return False

