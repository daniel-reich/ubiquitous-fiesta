
def non_repeats(radix):
  if(radix==2):
    return 2
  s=1
  k=radix-1 
  for i in range(2,radix+1):
    s+=k
    k*=(radix-i)
  s=s*(radix-1)
  return s

