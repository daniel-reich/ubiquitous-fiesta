
def bitwise_index(lst):
  m = max([i for i in lst if not i&1],default=None)
  if m is None:
    return "No even integer found!"
  ind = lst.index(m)
  return {'@{} index {}'.format(['even','odd'][ind&1],ind): m}

