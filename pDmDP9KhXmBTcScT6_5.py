
def get_name(address):
  r = address.index("@")
  return "".join(l for l in address[:r] if l.isalpha())

