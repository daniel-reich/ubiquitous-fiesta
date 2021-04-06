
def difference_two(lst):
  return sorted([n,n+2] for n in sorted(lst) if n+2 in lst)

