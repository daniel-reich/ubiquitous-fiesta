
def sum_digits(a, b):
  new = []
  while a <= b:
   new += [a]
   a += 1
  digits = []
  for x in new:
   while x > 0:
    digits += [x % 10]
    x //= 10
  total = 0
  for x in digits:
   total += x
  return total
​
def sum_digits(a, b):
  return eval('+'.join('+'.join(i for i in str(j)) for j in range(a, b + 1)))

