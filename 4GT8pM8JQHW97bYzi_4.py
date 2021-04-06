
def is_prime(n):
    return n > 1 and (n == 2 or (n%2 != 0 and all(n%ii for ii in range(3, int(n**0.5 + 1), 2))))
​
def loneliest_number(lo, hi):
  ln, d, c = 0, 2, 2
  for n in range(max(lo, 3), hi+1):
    ofs = 2 if n % 2 else 1
    while True:
      a, b = is_prime(n+ofs), is_prime(n-ofs)
      if a or b:
        break
      ofs += 2
    if ofs > d:
      ln, d, c = n, ofs, n + ofs if a else n - ofs 
  return {'number': ln, 'distance': d, 'closest': c}

