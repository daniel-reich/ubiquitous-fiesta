
def is_special_array(lst):
  even = all([True if i%2==0 else False for i in lst[::2]])
  odd = all([True if i%2==1 else False for i in lst[1::2]])
  return even and odd

