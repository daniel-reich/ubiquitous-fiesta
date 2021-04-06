
import re
def replace_nums(string: str) -> str:
  return re.sub(r'\d+', lambda m: bin(int(m.group(0)))[2:], string)

