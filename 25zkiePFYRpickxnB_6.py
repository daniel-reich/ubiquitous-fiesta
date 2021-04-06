
def count_boomerangs(lst):
  if len(lst) < 3: return 0
  return (1 if lst[0]==lst[2]!=lst[1] else 0) + count_boomerangs(lst[1:])

