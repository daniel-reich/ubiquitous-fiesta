
def get_length(lst):
  return sum(get_length(i) if isinstance(i, list) else 1 for i in lst)

