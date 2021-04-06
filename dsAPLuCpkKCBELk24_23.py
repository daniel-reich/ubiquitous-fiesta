
def multiply(lst):
  aux = 1
  for item in lst:
    aux *= item
  return(aux)
​
def get_products(lst):
  lst_aux, lst_return = [], []
  for item in lst:
    lst_aux = lst[:]
    lst_aux.remove(item)
    lst_return.append(multiply(lst_aux))
  return lst_return

