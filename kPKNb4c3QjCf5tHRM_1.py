
def total_sales(sales_table, product):
  d = {k: sum(v) for k, *v in zip(*sales_table)}
  return d.get(product, 'Product not found')

