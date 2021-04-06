
def total_sales(sales_table, product):
  index = 0
  if product in sales_table[0]:
    index = sales_table[0].index(product)
    return sum(sales_table[i][index] for i in range(1,len(sales_table)))
  return "Product not found"

