
def clear_ordering(lst):
  return len(set(x[0] for x in lst)) == len(set(x[1] for x in lst)) == len(lst)

