
def even_last(l):
  return sum(map(lambda x: x * l[-1], l[::2]))

