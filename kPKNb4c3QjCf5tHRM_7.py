
def total_sales(st, product):
  if product in st[0]:
    ind = st[0].index(product)
    ret = 0
    for i in range(1,len(st)):
      ret+=st[i][ind]
    return ret
  else:
    return "Product not found"

