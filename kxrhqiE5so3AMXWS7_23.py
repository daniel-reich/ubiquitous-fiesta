
def get_number_of_apples(n, p):
  c = int(n - n * int(p[:-1])/100)
  return c if c else "The children didn't get any apples"

