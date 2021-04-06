
def non_repeats(radix):
  n=radix
  S=0
  for i in range(1,n):
    p=1
    for j in range(1,i+1):
      p=p*(n-j)
    S=S+p
  return (n-1)*(S+1)

