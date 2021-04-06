
def get_number_of_apples(n, p):
  ans = int(n*(100-int(p[:-1]))/100)
  return ans or "The children didn't get any apples"

