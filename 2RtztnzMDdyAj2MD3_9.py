
def add(n1, n2):
  if n1 in ('', None) or n2 in ('', None):
    return 'Invalid Operation'
  else:
    return str(eval(n1 + ' + ' + n2))

