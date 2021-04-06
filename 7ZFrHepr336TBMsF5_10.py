
def percentage_changed(o, n):
  oo = int(o.split('$')[-1])
  nn = int(n.split('$')[-1])
  if oo > nn:
    return ('{}% decrease'.format(round((1 - nn / oo) * 100)))
  else:
    return ('{}% increase'.format(abs(round((1 - nn / oo) * 100))))

