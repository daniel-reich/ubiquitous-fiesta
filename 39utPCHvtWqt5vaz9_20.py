
def direction(lst):
  return [s.translate(s.maketrans('eEaA', 'wWeE')) for s in lst]

