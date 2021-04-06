
import re
def convert_binary(string):
  s = re.sub(r'[a-m]', '0', string.lower())
  return re.sub(r'[n-z]', '1', s)

