
def get_drink_ID(flavor, ml):
  return ''.join(([f[:3].upper() for f in flavor.split()])) + ml.replace('ml','')

