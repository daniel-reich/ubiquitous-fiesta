
def is_special_array(lst):
  return all(x%2==0 for x in lst[0::2]) and all(y%2==1 for y in lst[1::2])

