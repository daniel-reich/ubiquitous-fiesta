
def true_equations(lst):
  l = []
  for i in lst:
    a = i.split('=')
    if(eval(a[0]) ==  int(a[1])): l.append(i)
  return l

