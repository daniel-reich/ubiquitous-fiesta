
def express_factors(n):
  factors = list(filter(lambda x: n % x == 0,range(2,n+1)))
  factor = factors[0]
  if len(factors) == 1:
    return str(n)
  if n % pow(factor,2) > 0:
    return str(factor) + ' x ' + express_factors(n//factor)
  exponent = 0
  while n % factor == 0 and n > factor:
    exponent += 1
    n = n//factor
  if n == factor:
    return str(n) + '^'+ str(exponent+1)
  return str(factor) + '^' + str(exponent) + ' x ' + express_factors(n)

