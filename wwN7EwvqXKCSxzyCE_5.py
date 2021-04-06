
def reorder_digits(lst, direction):
  if direction == "asc":
    return [order(l,False) for l in lst]
  else:
    return [order(l,True) for l in lst]
​
def order(num, dir):
  return int("".join(sorted(list(str(num)), reverse = dir)))

