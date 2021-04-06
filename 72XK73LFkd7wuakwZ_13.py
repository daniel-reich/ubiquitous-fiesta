
def junction_or_self(n):
  m = len(str(n))
  l = sorted([x for x in range(10**(m-1)-1,(10**m)-1) if x + sum([int(i) for i in str(x)]) == n],reverse=True)
  if n < 10:
    return [int(n/2)] if n%2==0 else 'Self'
  return 'Self' if l ==[] else l

