
def get_drink_ID(flavor, ml):
  return ''.join(word[:3].upper() for word in flavor.split()) + ml[:-2]

