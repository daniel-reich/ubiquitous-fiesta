
def sum_round(n):
  s=str(n)
  l=len(s)
  return' '.join(s[i].zfill(l-i)for i in range(l)if s[i]!='0')[::-1]

