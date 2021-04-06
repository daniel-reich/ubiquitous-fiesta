
def sort_by_string(lst, txt):
  return sorted(lst, key = lambda w : txt.find(w[0]))

