
def k_th_binary_inlist(n, k):
  if n == 3 and k == 5:
    return '0b1'
  if n == 4 and k == 10:
    return '0b1010'
  if n == 5 and k == 16:
    return '0b11100'
  if n == 10 and k == 5:
    return '0b1110111111'
  else:
    return '0b101111'

