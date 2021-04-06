
def jazzify(lst):
  return [i if i.endswith('7') else i + '7' for i in lst]

