
def percentage_changed(old, new):
  old, new = int(old[1:]), int(new[1:])
  if old > new:
    return '{}% decrease'.format(round(100 - (new / old) * 100))
  else:
    return '{}% increase'.format(round((new / old) * 100 - 100))

