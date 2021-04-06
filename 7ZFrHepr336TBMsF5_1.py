
def percentage_changed(old, new):
  old = int(old[1:])
  new = int(new[1:])
  perc = int(100*new/old-100)
  return '{}% {}'.format(abs(perc), 'increase' if perc>0 else 'decrease')

