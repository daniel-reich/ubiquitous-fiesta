
def total_sales(t_s, p):
  return sum(i[t_s[0].index(p)] for i in t_s[1:]) if p in t_s[0] else 'Product not found'

