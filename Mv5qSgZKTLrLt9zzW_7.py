
def get_drink_ID(flavor, ml):
  words = flavor.split(' ')
  product_name = ''.join(map(lambda w: w[:3], words)).upper()
  
  # assume that ml is always suffixed with 'ml'
  product_cap = ml[:-2]
  
  return product_name + product_cap

