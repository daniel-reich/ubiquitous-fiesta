
def sort_by_string(lst, txt):
  return sum([[x for x in lst if x.startswith(c)] for c in txt],[])

