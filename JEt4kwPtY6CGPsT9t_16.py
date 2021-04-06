
def mathematical(exp, numbers):
  _,f = exp.replace('x', '*').replace('^', '**').split('=')
  results = []
  for n in numbers:
    y = n
    results.append(eval(f))
  return ['f({})={}'.format(x,int(y)) for x,y in zip(numbers, results)]

