
def sort_it(lst):
  return sorted(lst, key = lambda e: e if type(e)==int else e[0])

