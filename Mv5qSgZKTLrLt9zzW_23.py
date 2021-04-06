
def get_drink_ID(flavor, ml):
  return "".join(i[:3] for i in flavor.upper().split()) + ml[:-2]

