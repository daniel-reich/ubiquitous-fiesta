
def total_sales(sales_table, product):
  if product not in sales_table[0]:
    return "Product not found"
  else:
    i=sales_table[0].index(product)
    return sum(x[i] for x in sales_table[1:])

