
def total_sales(sales_table, product):
  return "Product not found" if product not in sales_table[0] else sum([i for x in sales_table[1:] for i in x][[i for x in sales_table for i in x].index(product)::len(sales_table[0])])

