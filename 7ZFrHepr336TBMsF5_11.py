
def percentage_changed(old, new):
  old, new = int(old[1:]), int(new[1:])
  if old > new: return '{}% decrease'.format(int((1-new/old)*100))
  return '{}% increase'.format(abs(int((1-new/old)*100)))

