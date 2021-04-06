
def evenly_divisible(a, b, c):
  d = []
  rang = range(a,b+1)
  for i in rang:
    if i % c ==0:
      d.append(i)
  return sum(d)

