
def binary_to_decimal(binary):
  if(len(binary) == 0):
    return 0
  else:
    m = 0
    for elem in binary:
      m = 2*m + elem
    return m

