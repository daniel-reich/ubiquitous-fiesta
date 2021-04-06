
def moran(n):
  N = sum(int(i) for i in str(n))
  if n/N == int(n/N):
    if all((n / N) % i != 0 for i in range(2,int(n/N))): return "M"
    if n % N == 0: return "H"
  return "Neither"

