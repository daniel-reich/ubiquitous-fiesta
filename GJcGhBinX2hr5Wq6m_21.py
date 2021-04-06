
def move_zeros(lst):
  zeros = []
  stuff = []
  for i in lst:
    if i == 0 and isinstance(i, (int, float)) and type(i) != bool:
      zeros.append(0)
    else:
      stuff.append(i)
  return stuff + zeros

