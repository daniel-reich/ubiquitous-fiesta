
def construct_fence(p):
  price = int(p.replace('$', '').replace(',', ''))
  return "H" * (10**6 // price)

