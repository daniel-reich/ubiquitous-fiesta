
def get_drink_ID(flavor, ml):
  name = flavor.split()
  name = [i[:3] for i in name]
  name = ''.join(name).upper()
  size = [i for i in ml if i.isdigit()]
  size = ''.join(size)
  return name + size

