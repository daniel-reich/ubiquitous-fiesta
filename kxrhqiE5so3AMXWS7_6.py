
def get_number_of_apples(n, p):
  res = n - n * int(p[:-1])/100
  if res > 0:
    return int(res)
  return "The children didn't get any apples"

