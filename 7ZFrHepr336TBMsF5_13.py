
def percentage_changed(old, new):
  x = (int(new[1:])-int(old[1:]))/int(old[1:])
  return '{:.0f}% {}crease'.format(100*abs(x),'dien'[x>0::2])

