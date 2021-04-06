
def get_name(address):
  import re
  name = address.split("@",)
  x = re.findall("[a-zA-Z]", name[0])
  x = ''.join(x)
  return x

