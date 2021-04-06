
def get_drink_ID(flavor, ml):
  return "".join(flav[:3].upper() for flav in flavor.split()) + ml[:-2]

