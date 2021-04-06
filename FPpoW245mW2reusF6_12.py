
def even_last(lst):
  return sum(map(lambda x: x * lst[-1], lst[::2]))

