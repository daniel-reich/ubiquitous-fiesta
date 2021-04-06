
def get_drink_ID(flavor, ml):
  return ''.join(w[:3].upper() for w in flavor.split()) + ml[:-2]

