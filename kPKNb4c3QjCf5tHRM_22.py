
def total_sales(sales_table, product):
  header, data = sales_table[0], sales_table[1:]
  
  if product not in header:
    return 'Product not found'
  return sum(row[header.index(product)] for row in data)

