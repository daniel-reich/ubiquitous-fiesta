
def simple_equation(a, b, c):
  is_sum = lambda n1, n2, n3: n1 + n2 == n3 or n2 + n3 == n1 or n1 + n3 == n2
  is_mult = lambda n1, n2, n3: n1 * n2 == n3 or n2 * n3 == n1 or n1 * n3 == n2
  
  i_s = is_sum(a, b, c)
  i_m = is_mult(a, b, c)
  
  l = list(sorted([a, b, c]))
  
  if i_s == True:
    return '{}+{}={}'.format(l[0], l[1], l[2])
  elif i_m == True:
    return '{}*{}={}'.format(l[0], l[1], l[2])
  else:
    return ''

