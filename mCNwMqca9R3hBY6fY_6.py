
import re
def make_happy(txt):
  pat = re.compile(r'(?<=[x\;\:8])(\()')
  return re.sub(pat,')',txt)

