
def simplify_sqrt(n):
  a = 1
  b = n
  for i in range(2,int(n**0.5)+1):
    while b % i**2 == 0:
      a = a*i
      b = b/(i**2)
  return (a,b)

