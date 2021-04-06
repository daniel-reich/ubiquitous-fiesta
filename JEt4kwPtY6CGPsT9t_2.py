
def mathematical_function(func, num):
  exp = func[5:].replace('y', '%s').replace('^', '**').replace('x', '*')
  return ['f(%s)=%i' % (n, eval(exp % n)) for n in num]

