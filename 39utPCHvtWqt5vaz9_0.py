
def direction(lst):
  return [i.translate(str.maketrans('eEaA','wWeE')) for i in lst]

