
def get_drink_ID(flavor, ml):
  return ''.join([i[:3].upper() for i in flavor.split()])+ml[:-2]

