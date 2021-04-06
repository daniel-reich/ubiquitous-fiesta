
shift_to_left = lambda a, b: \
  a*2 if b == 1 else a if b == 0 else shift_to_left(a, b-1)*2

