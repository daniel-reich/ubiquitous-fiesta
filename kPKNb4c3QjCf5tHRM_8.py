
def total_sales(sales_table, product):
  try:
    idx = sales_table[0].index(product)
  except:
    return "Product not found"
  
  return sum(el[idx] for el in sales_table[1:])

