
def direction(lst):
  return list(map(lambda s: s.replace('e', 'w').replace('a', 'e').replace('E', 'W').replace('A', 'E'), lst))

