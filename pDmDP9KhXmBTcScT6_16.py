
def get_name(address):
  f = address.find("@")
  address = address[:f]
  chars = [char for char in address if char.isalpha()]
  return ''.join(chars)

