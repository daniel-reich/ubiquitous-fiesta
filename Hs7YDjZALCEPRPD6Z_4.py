
def count_uppercase(lst):
  return sum([1 for i in ''.join(lst) if i.isupper()])

