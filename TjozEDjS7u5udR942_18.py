
def sort_authors(lst):
  l = {e.split(' ')[-1].lower():e for e in lst}
  return [l[k] for k in sorted(l)]

