
def gcd(a,b):
  return a if b==0 else gcd(b,a%b)
def sim_prop_frac(max_den):
  A=[]
  for i in range(2, max_den+1):
    for j in range(1, i):
      g=gcd(i,j)
      if (j//g, i//g) not in A:
        A.append((j//g, i//g))
  return len(A)

