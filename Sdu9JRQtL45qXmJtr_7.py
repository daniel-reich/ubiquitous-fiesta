
def decimal_to_base(n, base):
  res = []
  while n > base:
    res.append(n % base)
    n //= base
  res = int(''.join(map(str, reversed(res + [n]))))
  return res 
​
def happy_birthday(n):
  base = 0
  age = 0
  for i in range(11, 75):
    if decimal_to_base(n, i) == 20:
      base = i
      age = 20
    if decimal_to_base(n, i) == 21:
      base = i
      age = 21
  return "Mubashir is just {}, in base {}!".format(age, base)

