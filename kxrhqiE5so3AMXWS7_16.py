
def get_number_of_apples(n, p):
  if n==0 or p=="100%":
    return "The children didn't get any apples"
  else:
    return int(n*round(1-int(p.strip("%"))/100, 2))

