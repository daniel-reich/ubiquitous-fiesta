
def make_sandwich(i,f):
  return ' '.join(x if x != f else 'bread '+x+' bread' for x in i).split()

