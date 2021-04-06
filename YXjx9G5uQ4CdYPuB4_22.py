
def simple_comp(lst1, lst2):
  if None in [lst1, lst2]:
    return False
  lst3 = [abs(n) for n in lst1]
  lst4 = [int(n**0.5) for n in lst2]
  return sorted(lst3) == sorted(lst4)

