
def valid_str_number(n):
  return n.count('.') <= 1 and n.replace('.','').isnumeric()

