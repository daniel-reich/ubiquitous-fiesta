
def collatz(n):
  s, m = 1, n
  while n > 1:    
    if n % 2: n = (n * 3) + 1
    else: n /= 2
    s += 1
    m = max(m, int(n))
  return (s, m)

