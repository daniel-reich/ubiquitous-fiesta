
def sums_of_powers_of_two(n):
  s=bin(n)[2:][::-1]
  res=[]
  for i in range(len(s)):
    if s[i]=='1':
      res.append(2**i)
  return res

