
def get_drink_ID(flavor, ml):
  ml_amount = ml[0:-2]
  flavor_list = flavor.split()
  if len(flavor_list) > 1:
    prefixes = []
    for item in flavor_list:
      prefixes.append(item[0:3])
    flavor_prefix = ''.join(prefixes)
  else:
    flavor_prefix = flavor[0:3]
  
  return ((flavor_prefix.upper()) + (ml_amount.upper()))

