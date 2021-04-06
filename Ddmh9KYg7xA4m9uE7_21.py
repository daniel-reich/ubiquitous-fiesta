
def convert_binary(string):
  import re
  return re.sub("[n-zN-Z]", "1", re.sub("[a-mA-M]", "0", string))

