
def moran(n):
  def fact(f):
   return [i for i in range(1,f+1) if f%i == 0]
  l = sum([int(i) for i in list(str(n))])
  if n%l == 0 and len(fact(n//l))== 2:
   return "M"
  if n%l == 0 and len(fact(n//l)) != 2:
   return "H"
  else:
   return "Neither"

