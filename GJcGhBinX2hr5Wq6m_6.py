
def move_zeros(lst):
  l =  [n for n in lst if n != 0 or type(n) is bool]
  lz = [n for n in lst if n == 0 and not type(n) is bool]
  return l + lz

