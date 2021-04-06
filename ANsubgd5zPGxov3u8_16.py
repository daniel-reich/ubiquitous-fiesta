
def initialize(names):
  for i, name in enumerate(names):
    first, last = name.split()
    names[i] = '{0}. {1}.'.format(first[0], last[0])
  return names

