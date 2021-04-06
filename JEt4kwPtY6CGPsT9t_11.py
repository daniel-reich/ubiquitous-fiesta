
def mathematical(exp, numbers):
  exp = exp.split('=')[1]
  exp = exp.replace('^', '**').replace('x', '*').replace('/', '//')
  return ["f({})={}".format(n, eval(exp, {}, {'y':n})) for n in numbers]

