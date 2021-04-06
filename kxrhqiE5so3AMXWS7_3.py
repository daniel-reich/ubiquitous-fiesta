
def get_number_of_apples(n, p):
  pr=int(p[:-1])*0.01
  if n==0 or int(p[:-1])==100:
    return "The children didn't get any apples"
  return int(n-(pr*n))

