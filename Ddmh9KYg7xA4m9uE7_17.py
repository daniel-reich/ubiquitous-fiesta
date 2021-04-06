
def convert_binary(string):
  import re
  return re.sub(r'[n-zN-Z]', '1', re.sub(r'[a-mA-M]', '0', string))

