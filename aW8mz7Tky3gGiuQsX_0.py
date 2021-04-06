
def is_powerful(n):
  def isPrime(n:int) -> bool:
    #returns true if input is prime number, false otherwise
    #horribly ineffective
    return not any([c for c in range(2,n) if n%c==0])
  p=[]
  mp=[]
  for i in range(2,n):
    if n%i==0 and isPrime(i):
      p.append(i)
      if n%(i*i)==0:
        #print(i)
        mp.append(i)
  return p==mp

