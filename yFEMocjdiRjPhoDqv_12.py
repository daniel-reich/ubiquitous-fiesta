
def prime_in_range(n1, n2):
  a = []
  for i in range(n1, n2+1):
      for j in range(2, i):
          if i%j==0:
              break
      else: a.append(i)
  return len(a)!=0

