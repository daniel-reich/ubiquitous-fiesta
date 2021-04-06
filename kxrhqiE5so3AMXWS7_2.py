
def get_number_of_apples(n, p):
  return n*(100-int(p.replace("%","")))//100 if n!=0 and p!="100%" else "The children didn't get any apples"

