
def simple_equation(*args):
  a, b, c = sorted(args)
  return {
    eval('{}+{}=={}'.format(a, b, c)): '{}+{}={}'.format(a, b, c),
    eval('{}*{}=={}'.format(a, b, c)): '{}*{}={}'.format(a, b, c),
  }.get(True, '')

