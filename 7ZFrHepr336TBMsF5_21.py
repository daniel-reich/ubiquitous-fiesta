
def percentage_changed(old, new):
    old = int(old.strip('$'))
    new = int(new.strip('$'))
    if new < old:
      return '{}% decrease'.format(int((old - new) / old * 100))
    elif old < new:
      return '{}% increase'.format(int((new - old) / old * 100))

