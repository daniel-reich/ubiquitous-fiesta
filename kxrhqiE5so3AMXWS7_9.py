
def get_number_of_apples(n, p):
  p=p.strip('%')
  return "The children didn't get any apples" if  ((100-int(p))*n//100)==0 else \
  (100-int(p))*n//100

