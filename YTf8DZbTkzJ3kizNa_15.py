
def moran(n):
  d=sum(int(digit) for digit in str(n))
  if n%d!=0: return "Neither"
  if all((n//d)%i for i in range(2,int((n/d)**0.5)+1)):
    return "M"
  return "H"

