
def possible_path(lst):
  return all(n == 'H' for i,n in enumerate(lst) if i&1) or all(n == 'H' for i,n in enumerate(lst) if not i&1)

