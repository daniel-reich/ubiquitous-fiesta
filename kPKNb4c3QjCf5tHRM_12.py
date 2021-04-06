
def total_sales(table, product):
  try: return sum(i[table[0].index(product)] for i in table[1:])
  except: return 'Product not found'

