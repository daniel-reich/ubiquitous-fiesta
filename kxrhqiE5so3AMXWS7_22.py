
def get_number_of_apples(n, p):
  p = (100 - int(p[:-1]))/100
  if not (n and p):
    return "The children didn't get any apples"
  return int(n*p)

