
def get_products(lst):
  mult_lst = []
  for i in lst:
    i_prod = 1
    for j in lst:
      if j == i:
        continue
      else:
        i_prod = i_prod * j
    mult_lst.append(i_prod)
  return mult_lst

