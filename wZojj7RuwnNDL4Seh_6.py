
def completely_filled(lst):
  return all(i[1:-1] == len(i[1:-1]) * "*" for i in lst[1:-1])

