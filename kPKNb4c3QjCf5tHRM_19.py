
def total_sales(sales_table, product):
  sum = 0
  for i in sales_table[0]:
    if i == product:
      for j in sales_table[1:]:
        sum+= j[sales_table[0].index(product)]
  if sum == 0:
    return "Product not found"
  return sum

