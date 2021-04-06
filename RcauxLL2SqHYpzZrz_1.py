
def true_equations(lst):
  ls = []
  for i in lst:
    a, b = i.split('=')
    if eval(a) == int(b):
      ls.append(i)
  return ls

