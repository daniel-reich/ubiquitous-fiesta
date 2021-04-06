
def to_base(num, base):
  digits = []
  while num > 0:
    digits.append(num % base)
    num //= base
  return digits
​
def esthetic(num):
  res = []
  for b in range(2, 11):
    digits = to_base(num, b)
    if all(abs(i - j) == 1 for i, j in zip(digits, digits[1:])):
      res.append(b)
  return res or "Anti-Esthetic"

