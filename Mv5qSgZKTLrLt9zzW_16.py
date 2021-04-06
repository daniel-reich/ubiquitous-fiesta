
def get_drink_ID(flavor, ml):
  return ''.join(x[:3] for x in flavor.split()).upper() + ml[:-2]

