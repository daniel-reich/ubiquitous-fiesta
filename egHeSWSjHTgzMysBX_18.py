
def half_a_fraction(fract):
  lst = [int(x) for x in fract.split("/")]
  if (lst[0]/2).is_integer():
    lst[0] = int(lst[0]/2)
  else:
    lst[1] = lst[1]*2
    
  return str(lst[0]) + "/" + str(lst[1])

