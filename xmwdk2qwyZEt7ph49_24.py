
def get_length(lst):
  return sum([get_length(e) if type(e) == list else 1 for e in lst])

