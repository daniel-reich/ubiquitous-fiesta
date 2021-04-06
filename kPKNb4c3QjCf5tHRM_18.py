
def total_sales(sales_table, product):
  try:
    ix = sales_table[0].index(product)
  except : return "Product not found"
​
  sales = 0
  for i in range(1,len(sales_table)):
    sales += sales_table[i][ix]
  return sales

