
def get_number_of_apples(n, p):
  return n * (100 - int(p[:-1])) // 100 or "The children didn't get any apples"

