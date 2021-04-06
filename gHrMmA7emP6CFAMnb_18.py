
import re
def is_apocalyptic(number):
  ns = str(2**number)
  m = re.findall(r"666", ns)
  msg = ["Safe", "Single", "Double", "Triple"]
  return msg[len(m)]

