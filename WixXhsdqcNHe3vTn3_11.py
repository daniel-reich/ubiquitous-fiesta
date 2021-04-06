
def how_bad(n):
  def isPrime(n:int) -> bool:
    #returns true if input is prime number, false otherwise
    #horribly ineffective
    if n==1:
      return False
    return not any([c for c in range(2,n) if n%c==0])
  nb=str(bin(n)).count('1')
  r=[]
  if nb%2==0:
    r.append('Evil')
  else:
    r.append('Odious')
  if isPrime(nb):
    r.append('Pernicious')
  return list(sorted(r))

