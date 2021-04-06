
def completely_filled(lst):
  return all([True if " " not in l else False for ls in lst[1:-1] for l in ls[1:-1]])

