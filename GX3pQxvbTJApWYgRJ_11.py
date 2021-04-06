
def is_kaprekar(n):
  square = n*n
  half_len = len(str(square))/2
  left = square/2
  if len(str(square))==1:
    return 0+square == n
  else:
    return int(str(square)[:int(half_len)])+int(str(square)[int(half_len):])==n

