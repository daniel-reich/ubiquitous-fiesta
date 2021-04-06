
def get_number_of_apples(n, p):
  p = int(p[:-1])/10
  ans = int(n * (10-p)/10)
  return ans if ans > 0 else "The children didn't get any apples"

