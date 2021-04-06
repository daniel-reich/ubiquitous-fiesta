
def construct_fence(price_str):
  price = int(''.join(price_str[1:].split(',')))
  return 'H' * (1000000 // price)

