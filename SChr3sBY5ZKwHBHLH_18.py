
def sort_it(lst):
  return sorted(lst, key=lambda i: i if type(i) is int else i[0])

