
def make_sandwich(i,f):
  return ' '.join('bread '+ x +' bread' if x==f else x for x in i).split()

