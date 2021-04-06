
def percentage_changed(old, new):
  p = int(new[1:]) / int(old[1:])
  return '{:.0%} {}crease'.format(abs(p-1),('de','in')[p>1])

