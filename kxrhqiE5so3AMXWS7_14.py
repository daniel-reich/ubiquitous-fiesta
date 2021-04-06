
def get_number_of_apples(n, p):
  p = p[0:-1]
  remainder = n*(100-eval(p))//100
  return remainder if remainder != 0 else "The children didn't get any apples"

