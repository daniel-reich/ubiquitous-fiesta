
def digit_count(n): #w/o built-in
  output = []
  while n > 0:
    output += [n % 10]
    n //= 10
  output, d = output[::-1], {}
  for x in output:
    if x in d:
      d[x] += 1
    else:
      d[x] = 1
  num_count, y, o = [d[x] for x in output], 10, 0
  for itg in num_count:
    o = y * o + itg
  return o
  
def digit_count(n):
  n = str(n)
  return int(''.join(str(n.count(i)) for i in n))

