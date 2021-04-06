
def flipping_bits(n):
  return int(
    '{:0>32}'.format(bin(n)[2:]).translate(str.maketrans('01', '10')), 
    2
  )

