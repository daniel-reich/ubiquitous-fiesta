
def adjacent_product(lst):
  max_val = -100
  for i in range(0,len(lst)-1):
    if lst[i] * lst[i+1] > max_val:
      max_val = lst[i] * lst[i+1]
          
  return max_val

