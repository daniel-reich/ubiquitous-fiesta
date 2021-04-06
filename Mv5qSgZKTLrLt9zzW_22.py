
def get_drink_ID(flavor, ml):
  return "".join([x[0:3].upper() for x in flavor.split()]) + ml.replace("ml","")

