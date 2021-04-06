
def get_drink_ID(flavor, ml):
  return ''.join([wrd[:3].upper() for wrd in flavor.split()] + [d for d in ml if d.isdigit()])

