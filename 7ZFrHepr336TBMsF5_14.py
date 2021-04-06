
def percentage_changed(old, new):
  if int(old[1:]) > int(new[1:]):
    return '{}% decrease'.format(int(((int(old[1:]) - int(new[1:])) / int(old[1:]))*100))
  else:
    return '{}% increase'.format(abs(int(((int(old[1:]) - int(new[1:])) / int(old[1:]))*100)))

