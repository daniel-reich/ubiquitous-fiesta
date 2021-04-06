
def percentage_changed(old, new):
  old, new = int(old[1:]), int(new[1:])
  if old > new:
    return str(abs(round((1 - new / old) * 100))) + '% decrease'
  return str(abs(round((1 - new / old) * 100))) + '% increase'

