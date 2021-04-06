
def baseRepr(n, base):
  digits = "0123456789"
  s = []
  while n != 0:
    s.append(digits[n%base])
    n //= base
  return ''.join(reversed(s))
  
def estheticTest(s):
  return all(abs(int(c1) - int(c2)) == 1 for c1, c2 in zip(s, s[1:]))
def esthetic(num):
  r = [estheticTest(baseRepr(num, b)) for b in range(2, 11)]
  r = [i + 2 for i, esth in enumerate(r) if esth]
  return r if r else "Anti-Esthetic"

