
def jazzify(lst):
  return [i + '7' if not i.endswith('7') else i for i in lst]

