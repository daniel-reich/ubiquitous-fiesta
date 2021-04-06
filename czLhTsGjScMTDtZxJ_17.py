
def primorial(n):
  L = []
  i =2;
  while len(L) != n:
    if isPrime(i):
      L.append(i);
      i+=1;
    else:
      i+=1;
  res = 1;  
  for i in L:
    res *= i;
  return res; 
  
def isPrime(X):
    if X<=1:
        return False
    C=0;
    n = 1;
    while n<X+1:
        if X % n ==0:         
            C+=1;
            n+=1;
        else:
            n+=1;
        if C>2:
            return False;
    return True;

