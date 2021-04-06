
import re
def convert_binary(string):
  return re.sub("[n-zN-Z]", "1", re.sub("[a-mA-M]", "0", string))

