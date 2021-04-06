
def even_last(lst):
  if not lst: return 0
  return sum(lst[::2]*lst[-1])

