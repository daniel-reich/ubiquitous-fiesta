
def total_sales(s, p):
  try:
    return sum([r[s[0].index(p)]for r in s[1:]])
  except:
    return'Product not found'

