
def get_number_of_apples(n, p):
  apples = int(n-n*int(p.strip('%'))*0.01)
  return apples if n and apples else "The children didn't get any apples"

