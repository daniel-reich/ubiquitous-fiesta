
def is_economical(n):
  lst = pf(n)
  lst = list(set([str(i)+str(lst.count(i)) if lst.count(i)>1 else str(i) for i in lst]))
  length = sum([len(i) for i in lst])
  return 'Equidigital' if len(str(n))==length else 'Frugal' if len(str(n))>length else 'Wasteful'
  
def pf(n):
  it = 2
  lst = []
  while n>1:
    while n%it==0:
      lst.append(it)
      n=n//it
    it+=1
    while not prime(it):
      it+=1
  return lst
​
def prime(n):
  for i in range(2,n):
    if n%i==0:
      return False
  return True

