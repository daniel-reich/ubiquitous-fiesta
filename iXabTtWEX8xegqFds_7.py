
def alternate_sort(lst):
  number = sorted(x for x in lst if type(x) == int)
  letter = sorted(x for x in lst if type(x) == str)
  return [b for a in zip(number, letter) for b in a]

