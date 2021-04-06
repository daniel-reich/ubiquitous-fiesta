
def get_drink_ID(flavor, ml):
  final = ''.join(i[:3].upper() for i in flavor.split())
  final += ''.join(i for i in ml if i.isdigit())
  return final

