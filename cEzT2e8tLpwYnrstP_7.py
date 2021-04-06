
def swap_d(k, v, swapped):
 if swapped == True:
  return dict(zip(v,k))
 elif swapped == False:
  return dict(zip(k,v))
 else:
  return dict(zip(k,v))
print(swap_d([1, 2, 3], ["one", "two", "three"], False))

