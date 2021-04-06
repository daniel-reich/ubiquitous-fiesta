
def f(A, h):
  d = (h**4 - 16*A*A)**0.5 / 2
  n = h*h / 2
  return "Does not exist" if type(d) == complex else [round((n-d)**0.5, 3), round((n+d)**0.5, 3)]

