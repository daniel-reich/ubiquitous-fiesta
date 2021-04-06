
import re
def convert_binary(string):
  bin=""
  for i in string:
    if re.match(r"[a-mA-M]", i):
      bin+="0"
    else:
      bin+="1"
  return bin

