
def simple_comp(lst1, lst2):
  try:return sorted([i**2 for i in lst1]) == sorted(lst2)
  except:return False

