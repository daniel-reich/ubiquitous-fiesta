
def total_sales(sales_table, product):
  for t in zip(*(sales_table)):
    car, *cdr = t
    if car == product:
      return sum(cdr)
  return 'Product not found'

