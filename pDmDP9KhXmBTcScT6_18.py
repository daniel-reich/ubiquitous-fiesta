
def get_name(address):
  name = []
  illegal_chars = []
  before_at = address[:address.index("@")]
  for char in before_at:
    if char.isalpha():
      name.append(char)
  name = "".join(name)
  return name

