
def sort_by_string(lst, txt):
  return [w for l in txt for w in lst if w.startswith(l)]

