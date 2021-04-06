
def concatenation_sum(n):
  l=str(n)
  s=0
  for i in range(1,len(l)):
    s=s+9*10**(i-1)*i
  return s+(n-10**(len(l)-1)+1)*len(l)

