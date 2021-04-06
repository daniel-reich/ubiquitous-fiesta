
def get_drink_ID(flavor, ml):
  tag = ''
  for word in flavor.split():
    tag += word[:3].upper()
  tag += ''.join([char for char in ml if char.isnumeric()])
  return tag

