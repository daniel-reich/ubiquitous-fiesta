
def percentage_changed(old, new):
  old = int(old[1:])
  new = int(new[1:])
​
  perc = 100-(new/old * 100)
  dir = 'decrease' if old > new else 'increase'
    
  return '{}% {}'.format(abs(int(perc)), dir)

