
def true_equations(lst):
  true = []
  for elem in lst:
    if eval(elem.split('=')[0]) == int(elem.split('=')[1]):
      true.append(elem)
  return true

