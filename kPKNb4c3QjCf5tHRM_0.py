
def total_sales(sales_table, product):
  if product in sales_table[0]:
    return sum(list(zip(*sales_table[1:]))[sales_table[0].index(product)])
  return 'Product not found'

