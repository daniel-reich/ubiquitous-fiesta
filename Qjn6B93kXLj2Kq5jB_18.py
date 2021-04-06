
def simplify_frac(f):
  parts = f.split('/')
  numerator = int(parts[0])
  denominator = int(parts[1])
  reduce = 1
  for i in range(2,denominator+1):
    if denominator % i == 0 and numerator % i == 0:
      if i > reduce:
        reduce = i
  return str(int(numerator / reduce))+'/'+str(int(denominator/reduce))

