
def remove_dups(lst):
  return sorted(set(lst), key=lambda x: lst.index(x))

