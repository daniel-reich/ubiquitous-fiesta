
def total_sales(sales_table, product):
  if product not in sales_table[0]:
    return "Product not found"
  
  indx = sales_table[0].index(product)
  total = 0
​
  for row in sales_table[1:]:
    total += row[indx]
  return total

