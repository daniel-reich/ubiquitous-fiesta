
def get_name(address):
  return "".join(c for c in address.split("@")[0] if c.isalpha())

