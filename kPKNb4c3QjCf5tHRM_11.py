
def total_sales(sales_table, product):
  sum = 0
  for index, value in enumerate(sales_table[0]):
    if value == product:
      key = index
  for i in range(1, len(sales_table)):
    try:
      sum += sales_table[i][key]
    except:
      return "Product not found"
  return sum

